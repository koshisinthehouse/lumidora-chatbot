import os
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GPT4AllEmbeddings
from langchain.vectorstores.faiss import FAISS

class LumidoraEmbedding:

    def __init__(self, datastore_dir: str, vectorstore_dir: str):
        self.datastore_dir = datastore_dir
        self.vectorstore_dir = vectorstore_dir
    
    def save_vector_db(self, vectorstore: FAISS):
        # Speichern des Vektorstores mit FAISS-spezifischen Funktionen
        FAISS.save_local(vectorstore, self.vectorstore_dir)
        print(f"Vektorstore gespeichert unter {self.vectorstore_dir}")
        
    def create_vector_db(self):
        loader = DirectoryLoader(self.datastore_dir, glob="**/*.*", loader_cls=TextLoader, show_progress=True,
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
        # Überprüfen, ob das Verzeichnis existiert
        if os.path.exists(self.vectorstore_dir) and os.path.isdir(self.vectorstore_dir):
            embeddings = GPT4AllEmbeddings()  # Erstellen der Embeddings
            return FAISS.load_local(folder_path=self.vectorstore_dir, embeddings=embeddings)
        else:
            # Wenn das Verzeichnis nicht existiert oder kein Verzeichnis ist, None zurückgeben
            print(f"Verzeichnis {self.vectorstore_dir} existiert nicht oder ist kein Verzeichnis.")
            return None