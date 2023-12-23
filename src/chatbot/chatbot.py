from gc import callbacks
import json
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate

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
        
        # Open Issue: https://github.com/langchain-ai/langchain/issues/7747
        self.callbacks = [StreamingStdOutCallbackHandler()]

    def run_chat(self, input_text, config_json):
        
        # parse the json string into a ChatbotConfiguration object
        configuration = LumidoraChatbotConfiguration.from_json(config_json)
        print("Configuration loaded with model path:", configuration.model_path)  # Print model path

        # Initialize the LLM with the model from configuration
        self.llm = GPT4All(
            model=configuration.model_path,
            callbacks=self.callbacks,
            verbose=True,
            streaming=True,
            backend="phi2",
        )

        # define response schemas and parser using the text_schemas from configuration
        self.parser = StructuredOutputParser.from_response_schemas(configuration.text_schemas)
        format_instructions = self.parser.get_format_instructions()

        # create prompt template
        prompt = PromptTemplate(template=configuration.template, input_variables=["input"], partial_variables={"format_instructions": format_instructions})
        llm_chain = LLMChain(prompt=prompt, llm=self.llm, verbose=True)

        # run the chain with input
        output =llm_chain(input_text)
        print(f"output: [[[ {output.get('text')} ]]]")

        # parse the output
        parsed_output = self.parser.parse(output.get('text'))
        #print(f"parsed output: [[[ {parsed_output} ]]]")

        output_json_string = json.dumps(parsed_output)
        #print(f"output_json_string: [[[ {output_json_string} ]]]")

        json_object = json.loads(output_json_string)
        #print("final json_object: [[[ {json_object} ]]]")

        return json_object


