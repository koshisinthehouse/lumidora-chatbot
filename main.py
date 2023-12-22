import os
import torch
from src.chatbot.basic_module import Chatbot


def maikn():
    print("Chatbot")

    # Specify the model path
    model_path = "C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf"

    # Create an instance of the Chatbot class
    chatbot = Chatbot(model_path)

    # Define template and input text

    input_text = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."

    # Run the chat using the defined template and input text
    output_dict = chatbot.run_chat(input_text)


from src.chatbot.ui.iface import GradioApp

from src.chatbot.lumidora import Lumidora


import uvicorn


import threading

import tempfile


def prepare():
    temp_path = tempfile.gettempdir()
    print("Temporäres Verzeichnis:", temp_path)
    # Pfad für den neuen Unterordner erstellen
    app_temp_dir = os.path.join(temp_path, "Lumidora")
    # Unterordner erstellen, wenn er nicht bereits existiert
    if not os.path.exists(app_temp_dir):
        os.makedirs(app_temp_dir)
        print(f"Unterordner erstellt: {app_temp_dir}")
    else:
        print(f"Unterordner existiert bereits: {app_temp_dir}")
    

def main():
    

    lumidora = Lumidora()
    lumidora.create_directories()
    lumidora.add_agent("Agent1")
    agent = lumidora.get_agent("Agent1")
    if agent:
        print(f"Gefunden: {agent.name}")
    agent.open_agent_directory()
    
       
    agent.add_text(text="Ein KAKADUA ist ein schwarzes rundes Loch.",destination="temp")
    
    
    #lumidora.remove_agent("Agent1")


    prepare()
    #vec = LumidoraVectorDB()


    #app = GradioApp()
    #app.run()


# Pfad des temporären Verzeichnisses erhalten


    #uvicorn.run("src.chatbot.api.fastapi:app", host="0.0.0.0", port=8000, reload=True)
    #print("api started.")
    
    
    #print("Vektor")

    #device = 'cuda' if torch.cuda.is_available() else 'cpu'
    #print(f"Verwendetes Gerät: {'cuda'}")

        # Initialisieren Sie das Modell mit GPU-Unterstützung
    #model = HuggingfaceModel('gpt2').to(device)

    
    # Create an instance of the Chatbot class
    #vec = LumidoraVectorDB("C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf", "")
    #vec = LumidoraVectorDB("./vector_db.faiss")
    #vec.create_vector_db("./datastore")

    # Define template and input text

    

    # Run the chat using the defined template and input text
    

if __name__ == "__main__":
    main()