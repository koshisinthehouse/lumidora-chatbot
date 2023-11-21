from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot.chatbot_basic_module import Chatbot

app = FastAPI()

class BasicPrompt(BaseModel):
    prompt: str = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."


class BasicPromptResopnse(BaseModel):
    prompt: BasicPrompt
    answer: str


@app.post("/", response_model=BasicPromptResopnse)
async def prompt(basicPrompt: BasicPrompt) -> BasicPromptResopnse:
    print("Chatbot")

    # Specify the model path
    model_path = "D:/Lumidora/resources/llm/mistral-7b-openorca.Q4_0.gguf"

    # Create an instance of the Chatbot class
    chatbot = Chatbot(model_path)

    # Define template and input text

    # Run the chat using the defined template and input text
    output_dict = chatbot.run_chat(basicPrompt.prompt)

    return BasicPromptResopnse(prompt=basicPrompt, answer=output_dict)
