from fastapi import APIRouter, Depends
from chatbot.chat import LumidoraChatbot
from pydantic import BaseModel, constr

router = APIRouter(prefix="/basic")

class BasicPrompt(BaseModel):
    prompt: constr(max_length=2048) = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."

class BasicPromptResopnse(BaseModel):
    prompt: BasicPrompt
    answer: str

@router.post("/", response_model=BasicPromptResopnse)
async def prompt(basicPrompt: BasicPrompt) -> BasicPromptResopnse:
    print("Chatbot")

    # Specify the model path
    model_path = "C:/_dev/repositories/Lumidora/resources/llm/resources/openchat_3.5.Q4_K_M.gguf"

    # Create an instance of the Chatbot class
    chatbot = LumidoraChatbot(model_path)

    # Define template and input text

    # Run the chat using the defined template and input text
    json = chatbot.run_chat(basicPrompt.prompt)

    return BasicPromptResopnse(prompt=basicPrompt, answer=json)