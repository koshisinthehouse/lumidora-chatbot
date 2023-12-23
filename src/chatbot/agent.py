import hashlib
import os
import shutil
import webbrowser
from src.chatbot.embedding import LumidoraEmbedding
from src.chatbot.chatbot import LumidoraChatbot

class LumidoraAgent:
    def __init__(self, name, base_dir):
        self.name = name
        self.base_dir = base_dir
        self.agent_dir = os.path.join(self.base_dir, name)
        self.datastore_dir = os.path.join(self.agent_dir, "datastore")
        self.temp_dir = os.path.join(self.agent_dir, "temp")
        self.result_dir = os.path.join(self.agent_dir, "result")

        # Erstellen der benötigten Verzeichnisse in einer Schleife
        for directory in [self.datastore_dir, self.temp_dir, self.result_dir]:
            os.makedirs(directory, exist_ok=True)

        # Definieren der Verzeichnisse als Instanzvariable
        self.directories = {
            "datastore": self.datastore_dir,
            "temp": self.temp_dir,
            "result": self.result_dir
        }

        self.vector_db = LumidoraEmbedding(vector_db_path=os.path.join(self.datastore_dir, "vector_db"))

    def open_agent_directory(self):
        print(f"Open {self.agent_dir}.")
        webbrowser.open(self.agent_dir)

    def question(self, text, config):
        chatbot = LumidoraChatbot();
        return chatbot.run_chat(text,config)

    def add_text(self, text, destination):
        if destination in self.directories:
            destination_dir = self.directories[destination]

            # Generieren eines Hash-Namens aus dem Textinhalt
            hash_object = hashlib.sha256(text.encode())  # Text muss kodiert werden
            hex_dig = hash_object.hexdigest()  # Erhalten des Hexadezimal-Digests des Hash
            file_name = f"{hex_dig}.txt"  # Erstellen des Dateinamens

            file_path = os.path.join(destination_dir, file_name)
            with open(file_path, 'w') as file:
                file.write(text)
            print(f"Text erfolgreich in {file_path} gespeichert.")
        else:
            print(f"{destination} ist kein gültiges Zielverzeichnis.")
            
    def add_item(self, item_path, destination):
        # Überprüfen, ob das Zielverzeichnis gültig ist
        if destination in self.directories:
            destination_dir = self.directories[destination]
            shutil.copy(item_path, destination_dir)
            print(f"Item {item_path} zum {destination.capitalize()} hinzugefügt.")
        else:
            print(f"{destination} ist kein gültiges Zielverzeichnis.")