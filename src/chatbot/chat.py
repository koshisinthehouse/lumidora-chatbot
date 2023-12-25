import json
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, RetrievalQA
from langchain.vectorstores.faiss import FAISS

from datastore.retrieval_qa.base import BaseRetrievalQA

class LumidoraChatbotConfiguration:
    def __init__(self, model_path:str, template:str, text_schemas:list[ResponseSchema]):
        self.model_path = model_path
        self.template = template
        self.text_schemas = text_schemas  # Now handling multiple text schemas

    @classmethod
    def from_json(cls, json_str:str):
        # Parse the JSON string into a dictionary
        config_dict = json.loads(json_str)
        print("Loaded configuration:", config_dict)  # Print the loaded configuration

        # Extract and instantiate all text schemas
        text_schemas_dicts = config_dict.pop("text_schemas")
        text_schemas:list[ResponseSchema] = []
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
            
    def run_chat(self, input_text:str, config:LumidoraChatbotConfiguration, vectorstore: FAISS|None):
        
        print("Configuration loaded with model path:", config.model_path)  # Print model path

        # Initialize the LLM with the model from configuration
        self.llm = GPT4All(
            model=config.model_path,
            callbacks=self.callbacks,
            verbose=True,
            streaming=True,
            max_tokens=2048,
            n_predict=2048,
            backend="llama",
        )

        # define response schemas and parser using the text_schemas from configuration
        self.parser = StructuredOutputParser.from_response_schemas(config.text_schemas)
        format_instructions = self.parser.get_format_instructions()

        # create prompt template
        prompt = PromptTemplate(template=config.template, input_variables=["context", "question"], partial_variables={"format_instructions": format_instructions})
        
        if(vectorstore):
            print("use vector store data.")
            chain_type_kwargs = {"prompt":prompt}
            qa:BaseRetrievalQA = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff",retriever=vectorstore.as_retriever(), chain_type_kwargs=chain_type_kwargs)
            output = qa.run(input_text)
        else:
            print("default query")
            llm_chain = LLMChain(prompt=prompt, llm=self.llm, verbose=True)
            output =llm_chain(input_text)
            output = output.get('text')
            print(f"output: [[[ {output} ]]]")
            
        # run the chain with input
    
        # parse the output
        parsed_output = self.parser.parse(str(output))
        #print(f"parsed output: [[[ {parsed_output} ]]]")

        output_json_string = json.dumps(parsed_output)
        #print(f"output_json_string: [[[ {output_json_string} ]]]")

        json_object = json.loads(output_json_string)
        #print("final json_object: [[[ {json_object} ]]]")

        return json_object


