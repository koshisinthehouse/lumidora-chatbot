import hashlib
import os
import shutil
import webbrowser
from  src.chatbot.embedding import LumidoraEmbedding
from  src.chatbot.chat import LumidoraChatbot, LumidoraChatbotConfiguration

class LumidoraAgent:
    def __init__(self, name:str, base_dir:str):
        self.name:str = name
        self.base_dir:str = base_dir
        self.agent_dir:str = os.path.join(self.base_dir, name)
        self.datastore_dir:str = os.path.join(self.agent_dir, "datastore")
        self.vectorstore_dir:str = os.path.join(self.agent_dir, "vectorstore")
        self.temp_dir :str= os.path.join(self.agent_dir, "temp")
        self.result_dir :str= os.path.join(self.agent_dir, "result")

        # Erstellen der benötigten Verzeichnisse in einer Schleife
        for directory in [self.datastore_dir, self.temp_dir, self.result_dir,self.vectorstore_dir]:
            os.makedirs(directory, exist_ok=True)

        # Definieren der Verzeichnisse als Instanzvariable
        self.directories = {
            "datastore": self.datastore_dir,
            "temp": self.temp_dir,
            "result": self.result_dir,
        }

        self.vector_db = LumidoraEmbedding(datastore_dir=self.datastore_dir, vectorstore_dir=self.vectorstore_dir)

    def create_vectorstore(self):
        self.vector_db.create_vector_db()

    def open_agent_directory(self):
        print(f"Open {self.agent_dir}.")
        webbrowser.open(self.agent_dir)

    def question(self, text: str, config:LumidoraChatbotConfiguration):
        chatbot = LumidoraChatbot();
        return chatbot.run_chat(text,config,self.vector_db.load_vector_db())

    def add_text(self, text:str)->None:
        destination_dir = self.directories["datastore"]
        # Generieren eines Hash-Namens aus dem Textinhalt
        hash_object = hashlib.sha256(text.encode())  # Text muss kodiert werden
        hex_dig = hash_object.hexdigest()  # Erhalten des Hexadezimal-Digests des Hash
        file_name = f"{hex_dig}.txt"  # Erstellen des Dateinamens

        file_path = os.path.join(destination_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Text erfolgreich in {file_path} gespeichert.")
            
    def add_item(self, item_path:str, destination:str):
        # Überprüfen, ob das Zielverzeichnis gültig ist
        if destination in self.directories:
            destination_dir = self.directories[destination]
            shutil.copy(item_path, destination_dir)
            print(f"Item {item_path} zum {destination.capitalize()} hinzugefügt.")
        else:
            print(f"{destination} ist kein gültiges Zielverzeichnis.")
