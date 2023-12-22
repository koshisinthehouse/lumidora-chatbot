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


from src.chatbot.vectordb_module import LumidoraVectorDB

from src.chatbot.ui.iface import GradioApp


import uvicorn


import threading



def main():


    #t1 = threading.Thread(target=uvicorn.run, args=("src.chatbot.api.fastapi:app",), kwargs={"host": "0.0.0.0", "port": 8000}, daemon=True)
    #t2 = threading.Thread(target=gradio_app)

    #t1.start()
    #t2.start()

    #t1.join()
    #t2.join()

    app = GradioApp()
    app.run()



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