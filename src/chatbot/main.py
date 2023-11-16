from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.chains import  LLMChain
from langchain.prompts import PromptTemplate

from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser



def main():
    print("chatbot")
    print("chatbot")

    # Callbacks support token-wise streaming
    callbacks = [StreamingStdOutCallbackHandler()]

    model_path = "D:/Lumidora/resources/llm/mistral-7b-openorca.Q4_0.gguf"
    # model_path = "D:/Lumidora/resources/llm/openchat_3.5.Q4_K_M.gguf"

    # initialize the LLM and make chain it with the prompts
    llm = GPT4All(
        model=model_path,
        callbacks=callbacks,
        backend="llama",
    )

    text_schema = ResponseSchema(name="translation", description="The translated text")
    response_schemas = [text_schema]

    parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = parser.get_format_instructions()

    # run the chain with your query (text)
    template = "Enten"

    template = """ 
    You are an employee of a professional translation agency and receive a text in German.
    You are asked to translate this text into perfect English.
    Here is the German text you have to translate: {input}
    
    {format_instructions}
    
    """
    prompt = PromptTemplate(
    template=template,
    input_variables=["input"],
    partial_variables={"format_instructions": format_instructions}
    )

    message =prompt.format_prompt(input="Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild.")

    # paste the path where your model's weight are located (.bin file)
    # you can download the models by going to gpt4all's website.
    # scripts for downloading is also available in the later
    # sections of this tutorial







    #llm_chain.run(text)
    output = llm(message.to_string())
    #llm_chain('Who is the CEO of Google and why he became the ceo of Google?')

    print(output)

    output_dict = parser.parse(output)

    # Hier kannst du das Dictionary speichern, zum Beispiel in einer JSON-Datei
    import json

    #output_dict_path = "output_dict.json"
    #with open(output_dict_path, "w", encoding="utf-8") as json_file:
        #json.dump(output_dict, json_file, ensure_ascii=False, indent=4)