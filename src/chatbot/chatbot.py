import json
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from typing import Any, Dict, List, Union, Optional
from langchain.callbacks.base import BaseCallbackManager
from uuid import UUID
from langchain.agents import initialize_agent, load_tools
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction
from langchain.schema.output import ChatGenerationChunk, GenerationChunk

class MyCustomHandlerOne(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        print(f"on_llm_start {serialized}")

    async def on_llm_new_token(
        self,
        token: str,
        *,
        verbose:any,
        chunk: Optional[Union[GenerationChunk, ChatGenerationChunk]] = None,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
    ) -> None:
        print(f"on_new_token {token}")

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""

    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        print(f"on_chain_start {serialized}")

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        print(f"on_tool_start {serialized['name']}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        print(f"on_agent_action {action}")
        
class LumidoraChatbotConfiguration:
    def __init__(self, model_path, template, text_schemas):
        self.model_path = model_path
        self.template = template
        self.text_schemas = text_schemas  # Now handling multiple text schemas

    @classmethod
    def from_json(cls, json_str):
        # Parse the JSON string into a dictionary
        config_dict = json.loads(json_str)
        print("Loaded configuration:", config_dict)  # Print the loaded configuration

        # Extract and instantiate all text schemas
        text_schemas_dicts = config_dict.pop("text_schemas")
        text_schemas = []
        for schema in text_schemas_dicts:
            text_schema = ResponseSchema(name=schema["name"], description=schema["description"])
            text_schemas.append(text_schema)
            print(f"Added text schema: {text_schema.name} - {text_schema.description}")  # Print each text schema

        # Create a new instance of the class using the dictionary
        return cls(model_path=config_dict["model_path"], template=config_dict["template"], text_schemas=text_schemas)


class LumidoraChatbot:
    def __init__(self):
        self.callbacks = [MyCustomHandlerOne()]
        
        self.callback_manager = BaseCallbackManager([MyCustomHandlerOne()])
        

    def run_chat(self, input_text, config_json):
        # Parse the JSON string into a ChatbotConfiguration object
        configuration = LumidoraChatbotConfiguration.from_json(config_json)
        print("Configuration loaded with model path:", configuration.model_path)  # Print model path

        # Initialize the LLM with the model from configuration
        self.llm = GPT4All(
            model=configuration.model_path,
            callback_manager=self.callback_manager,
            verbose=True,
            streaming=True,
            backend="llama",
        )

        # Define response schemas and parser using the text_schemas from configuration
        self.parser = StructuredOutputParser.from_response_schemas(configuration.text_schemas)
        print("Initialized StructuredOutputParser with the following text schemas:")
        for schema in configuration.text_schemas:
            print(f"- Name: {schema.name}, Description: {schema.description}")

        # Generate prompt using the template from configuration
        format_instructions = self.parser.get_format_instructions()
        prompt = PromptTemplate(
            template=configuration.template,
            input_variables=["input"],
            partial_variables={"format_instructions": format_instructions}
        )
        message = prompt.format_prompt(input=input_text)
        print("Generated prompt:", message.to_string())  # Print the generated prompt


        # Run the chat with the given input
        output=""
        #output = self.llm(message.to_string())
        #print("Model output:", output)  # Print the raw model output
        
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        print(llm_chain.run(message.to_string()))
        

        # Parse the output
        output_dict = self.parser.parse(output)
        print("Parsed output:", output_dict)  # Print the parsed output

        output_json_string = json.dumps(output_dict)
        json_object = json.loads(output_json_string)
        print("Final JSON object:", json_object)  # Print the final JSON object

        return json_object  # Return the whole parsed object

