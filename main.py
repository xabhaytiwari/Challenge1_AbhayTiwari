from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseModel
from Qwen_tts import get_audio


class Sentence(BaseModel):
    sentence: str
    instructions: Optional[str] = None

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/process")
async def process_text(data: Sentence):

    print("MODEL FIELDS:", data.model_fields)
    sentence = data.sentence
    instructions = data.instructions

    get_audio(sentence, instructions)

    audio_url = "/static/output.wav"

    return {"audio_url": audio_url}