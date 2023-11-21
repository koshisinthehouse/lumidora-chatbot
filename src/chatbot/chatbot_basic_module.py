import json

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate


class Chatbot:

    def __init__(self, model_path):
        self.model_path = model_path
        self.callbacks = [StreamingStdOutCallbackHandler()]

        # Initialize the LLM
        self.llm = GPT4All(
            model=self.model_path,
            callbacks=self.callbacks,
            backend="llama",
        )

        # Define response schemas and parser
        text_schema = ResponseSchema(name="translation", description="The translated text")
        self.response_schemas = [text_schema]
        self.parser = StructuredOutputParser.from_response_schemas(self.response_schemas)

    def run_chat(self, input_text):
        template = """
    You are an employee of a professional translation agency and receive a text in German.
    You are asked to translate this text into perfect English.
    Here is the German text you have to translate: {input}
    
    {format_instructions}
    """

        # Generate prompt
        format_instructions = self.parser.get_format_instructions()
        prompt = PromptTemplate(
            template=template,
            input_variables=["input"],
            partial_variables={"format_instructions": format_instructions}
        )
        message = prompt.format_prompt(input=input_text)

        # Run the chat with the given input
        output = self.llm(message.to_string())
        print(output)

        # Parse the output
        output_dict = self.parser.parse(output)
        return output_dict

        # Save the output dictionary to a JSON file
        #output_dict_path = "output_dict.json"
        #with open(output_dict_path, "w", encoding="utf-8") as json_file:
            #json.dump(output_dict, json_file, ensure_ascii=False, indent=4)


