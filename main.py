import torch
from src.chatbot.basic_module import Chatbot


def main():
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

def mainkkk():
    print("Vektor")

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Verwendetes Gerät: {'cuda'}")

        # Initialisieren Sie das Modell mit GPU-Unterstützung
    #model = HuggingfaceModel('gpt2').to(device)

    # Specify the model path
    model_path = "C:/_dev/repositories/Lumidora/resources/llm/resources/mistral-7b-openorca.Q4_0.gguf"

    # Create an instance of the Chatbot class
    vec = LumidoraVectorDB(model_path)

    # Define template and input text

    

    # Run the chat using the defined template and input text
    output_dict = vec.run()

if __name__ == "__main__":
    main()