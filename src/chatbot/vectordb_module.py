from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.llms import GPT4All
from langchain.chains import RetrievalQA

import pickle

class Vec:

    def __init__(self, model_path):
        self.model_path = model_path

        # Initialize the LLM
        self.llm = GPT4All(
            model=self.model_path,
            backend="llama",
            max_tokens=4096
        )

    def run(self):

        # Loaders
        # Um Daten mit einem LLM zu verwenden, müssen Dokumente zunächst in eine Vectordatenbank. Der erste Schritt ist diese über einen Loader in memory zu laden
        text_loader_kwargs={'autodetect_encoding': True}
        #, loader_kwargs=text_loader_kwargs
        loader = DirectoryLoader('./datastore', glob="**/*.py", loader_cls=TextLoader, show_progress=True, loader_kwargs=text_loader_kwargs)
        docs = loader.load()
        print("Dokumente geladen.")

        # Text Splitter
        # Texte werden nicht 1:1 in die Datenbank geladen, sondern in Stücken, sog. "Chunks". Man kann die Chunk Größe und den Overlap zwischen den Chunks definieren
        from langchain.text_splitter import RecursiveCharacterTextSplitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
        )
        documents = text_splitter.split_documents(docs)
        print("Chunks erstellt.")


        # Embeddings
        # Texte werden nicht als Text in der Datenbank gespeichert, sondern als Vectorrepräenstation. Embeddings sind eine Art von Wortdarstellung, die die semantische Bedeutung von Wörtern in einem Vektorraum darstellt.
        from langchain.embeddings import GPT4AllEmbeddings
        embeddings = GPT4AllEmbeddings()
        

        # Laden der Vectoren in die VectorDB (FAISS)
        from langchain.vectorstores.faiss import FAISS
        vectorstore = FAISS.from_documents(documents, embeddings)

        print("Vektorstore erstellt aus Dokumente")

        #with open("vectorstore.pkl", "wb") as f:
            #pickle.dump(vectorstore, f)

        # PROMPT
        from langchain.prompts import PromptTemplate
        prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
        {context}
        Question: {question}"""
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        # Chains
        chain_type_kwargs = {"prompt": PROMPT}
        qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=vectorstore.as_retriever(), chain_type_kwargs=chain_type_kwargs)
        query = "Bitte zeige mir anhand eines Codebeispiels wie man die Methode from_chain_type der Klasse RetrievalQA benutzt."
        retval = qa.run(query)
        print(f"RetrievalQA object created:",retval)








        return "translation"
