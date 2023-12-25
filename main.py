import os


def maikn():
    print("Chatbot")

    # Specify the model path
    model_path = "C:/_dev/repositories/Lumidora/resources/llm/resources/ggml-model-q4_0.bin"



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
    #agent.open_agent_directory()
    
       
    agent.add_text(text=""" 22.12.2023: BITORIO ist super. Er wird immer besser werden. 24.12.2023 BITORIO ist schlecht, ich denke er wird schlechter.""")
    
    
    agent.create_or_update_vectorstore();
    
    
    config_json = """
    {
        "model_path": "C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf",
        "template": "Interprete the text and evaluate the text. sentiment: is the text in a positive, neutral or negative sentiment? subjdect: What subject is the text about? Use exactly one word. Just return the JSON, do not add ANYTHING, NO INTERPRETATION!\\n text: {input} \\n{format_instructions}",
        "text_schemas": [
            {
                "name": "sentiment",
                "description": "Is the text positive, neutral or negative? Only provide these words"
            },
            {
                "name": "subject",
                "description": "What subject is the text about? Use exactly one word."
            }
        ]
    }
    """

    text = "I ordered Pizza Salami for 9.99$ and it was awesome!"
    
    
    template = """
    
    Du bist ein hochqualifizierter Content-Ersteller, bekannt für die Produktion von viralen YouTube-Videos.
    Deine Aufgabe ist es, ansprechende und informative Inhalte zu erstellen, die mit der Zielgruppe resonieren und die Zuschauerbindung maximieren.
    Dein Video sollte SEO-optimiert sein, um das breiteste Publikum zu erreichen.
    Beginne damit, eine aufmerksamkeitserregende Einleitung zu gestalten, die den Zuschauer in den ersten Sekunden fesselt.
    Stelle sicher, dass die Einleitung direkt mit dem Videotema zusammenhängt und mindestens eines der Schlüsselwörter enthält.

    video_topic: the topic of the video
    keywords: top keywords in the video
    sentiment: is the text in a positive, neutral or negative sentiment?
    
    text: {input}
    
    {format_instructions}


    """
    
    config_json = """
    {
        "model_path": "c:/_dev/models/mistral-7b-openorca.Q8_0.gguf",
        "template": "You are a highly skilled content creator known for producing viral YouTube videos. Your task is to create engaging and informative content that resonates with the target audience and maximizes viewer engagement. Your video should be SEO-optimized to reach the widest audience possible.Begin by crafting an attention-grabbing introduction that hooks the viewer in the first few seconds. Ensure that the introduction is directly related to the video topic and includes at least one of the keywords.\\nvideo_topic: the topic of the video\\nkeywords: top words in the video\\nmain_text: the main text of the video\\n\\ntext: {input}\\n{format_instructions}",
        "text_schemas": [
            {
                "name": "video_topic",
                "description": "the video headline"
            },
            {
                "name": "keywords",
                "description": "main words in the video"
            },
            {
                "name": "sentiment",
                "description": ""What subject is the text about? Use exactly one word."
            }
        ]
    }
    """

    text = "Generiere ein Video über BITORIO und die aktuellsten BITORIO Finanzdaten."
    
    
    
   
    
    
    
    
    response = agent.question(text, config_json)
    print(response)

    
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