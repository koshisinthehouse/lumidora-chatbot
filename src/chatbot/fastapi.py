from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BasicPrompt(BaseModel):
    prompt: str = "Generiere eine hochwertige und realistische Illustration einer Comicfigur, die als Grundlage für künstliche Intelligenz auf einem YouTube-Kanal dienen soll. Die Figur soll eine fröhliche und freundliche Ausstrahlung haben, gepaart mit einem charismatischen Erscheinungsbild."


class BasicPromptResopnse(BaseModel):
    prompt: BasicPrompt
    answer: str


@app.post("/", response_model=BasicPromptResopnse)
async def prompt(basicPrompt: BasicPrompt) -> BasicPromptResopnse:
    return BasicPromptResopnse(prompt=basicPrompt, answer="")
