from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BasicPrompt(BaseModel):
    prompt: str


class BasicPromptResopnse(BaseModel):
    prompt: BasicPrompt
    answer: str

@app.post("/", response_model=BasicPromptResopnse)
async def prompt(basicPrompt: BasicPrompt) -> BasicPromptResopnse:
    return BasicPromptResopnse(prompt=basicPrompt, answer="")
