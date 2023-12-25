from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores.faiss import FAISS


class LumidoraEmbedding:

    def __init__(self, vector_db_path: str):
        self.vector_db_path = vector_db_path

    def save_vector_db(self, vectorstore: FAISS):
        # Speichern des Vektorstores mit FAISS-spezifischen Funktionen
        FAISS.save_local(vectorstore, self.vector_db_path)
        print(f"Vektorstore gespeichert unter {self.vector_db_path}")

    def create_vector_db(self, datastore_path: str):
        loader = DirectoryLoader(datastore_path, glob="**/*.py", loader_cls=TextLoader, show_progress=True,
                                 loader_kwargs={'autodetect_encoding': True})
        docs = loader.load()
        print("Dokumente geladen.")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        documents = text_splitter.split_documents(docs)
        print("Chunks erstellt.")
        embeddings = GPT4AllEmbeddings() # type: ignore
        vectorstore: FAISS = FAISS.from_documents(documents, embeddings)
        print("Vektorstore erstellt aus Dokumenten.")

        self.save_vector_db(vectorstore)

    def load_vector_db(self):
        embeddings = GPT4AllEmbeddings() # type: ignore
        return FAISS.load_local(folder_path=self.vector_db_path, embeddings=embeddings)

    def extend_vector_db(self, new_data_path: str):
        vectorstore = self.load_vector_db()

        loader = DirectoryLoader(new_data_path, glob="**/*.py", loader_cls=TextLoader, show_progress=True,
                                 loader_kwargs={'autodetect_encoding': True})
        new_docs = loader.load()
        print("Neue Dokumente geladen.")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        new_documents = text_splitter.split_documents(new_docs)
        print("Neue Chunks erstellt.")
        vectorstore.add_documents(new_documents)
        print("Vektorstore erweitert mit neuen Dokumenten.")
        self.save_vector_db(vectorstore)
