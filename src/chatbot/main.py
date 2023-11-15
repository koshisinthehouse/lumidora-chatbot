from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import GPT4All
from langchain.chains import  LLMChain
from langchain.prompts import PromptTemplate
def main():
    print("chatbot")
    print("chatbot")

    # create a prompt template where it contains some initial instructions
    # here we say our LLM to think step by step and give the answer

    template = """
    Mache einen Witz über {question}
    Witz:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # paste the path where your model's weight are located (.bin file)
    # you can download the models by going to gpt4all's website.
    # scripts for downloading is also available in the later
    # sections of this tutorial

    local_path = ("D:/Lumidora/resources/llm/openchat_3.5.Q4_K_M.gguf")

    # initialize the LLM and make chain it with the prompts

    # Callbacks support token-wise streaming
    callbacks = [StreamingStdOutCallbackHandler()]

    llm = GPT4All(
        model=local_path,
        callbacks=callbacks,
        backend="llama",
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    # run the chain with your query (question)
    question = "Enten"

    llm_chain.run(question)
    #llm_chain('Who is the CEO of Google and why he became the ceo of Google?')
