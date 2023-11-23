from src.chatbot.basic_module import Chatbot

def main():
    print("Chatbot")

    # Specify the model path
    model_path = "D:/Lumidora/resources/llm/mistral-7b-openorca.Q4_0.gguf"

    # Create an instance of the Chatbot class
    chatbot = Chatbot(model_path)

    # Define template and input text

    input_text = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."

    # Run the chat using the defined template and input text
    output_dict = chatbot.run_chat(input_text)

if __name__ == "__main__":
    main()