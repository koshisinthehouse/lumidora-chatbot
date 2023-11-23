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

        # run the chat with the given input
        output = self.llm(message.to_string())

        # parse the output
        output_dict = self.parser.parse(output)
        output_json_string = json.dumps(output_dict)
        json_object = json.loads(output_json_string)


        #Output PArser Fix: https://python.langchain.com/docs/modules/model_io/output_parsers/output_fixing_parser
        return json_object["translation"]
