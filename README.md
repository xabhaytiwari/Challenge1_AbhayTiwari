# The Empathy Engine
The Empathy Engine is an intelligent Text-to-Speech (TTS) web application that generates emotionally resonant audio, created as an Assignment for the role of AI Engineer at Darwix AI by **Abhay Tiwari**. By combining state-of-the-art sentiment analysis with a powerful TTS model, the application automatically detects the underlying emotion of the input text and renders the speech accordingly, allowing for custom user instructions to further refine the vocal delivery.

## Features
- **Emotion-Aware Audio Generation:** Utilizes the `j-hartmann/emotion-english-distilroberta-base model` to classify the sentiment of the input text automatically.
- **Custom Vocal Instructions:** Allows users to append specific directives (e.g., "whisper like a secret" or "shout") to guide the TTS generation.
- **Qwen3 TTS Integration:** Leverages the `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice model` to generate high-quality, customized voice outputs.
- **Sleek Terminal UI:** Features a minimalist, retro-hacker aesthetic(me) interface built with raw HTML, CSS, and JavaScript (not a web-developer!).
- **FastAPI Backend:** Provides a lightweight, asynchronous backend for processing requests and serving static files.

## Prerequisites
To run this project, you will need to have Conda (Miniconda or Anaconda) installed on your system to manage the dependencies.

## Installation
- **Clone the repository (or navigate to the project directory)**:
>`cd Challenge1_AbhayTiwari`
- **Create the Conda environment using the provided `environment.yml` file**:
>`conda env create -f environment.yml`
- **Activate the environment:**
>`conda activate the_empathy_engine`

## Usage
1. **Start the FastAPI server using Uvicorn:**
>`uvicorn main:app --reload`
2. **Access the Web Interface:**
Open your web browser and navigate to `http://127.0.0.1:8000.`
3. **Generate Audio:**
    - Enter the text you want to convert to speech in the sentence prompt.

    - (Optional) Enter any specific delivery style in the instructions prompt.

    - Click run_experiment() and wait for the model to process the audio. The resulting audio will play automatically and be available in the browser's audio player.

## Project Essentials (Apart from me!)
              
`├── environment.yml            # Conda environment specifications and dependencies`

`├── main.py                    # FastAPI server setup and routing`

`├── Qwen_tts.py                # Core TTS generation script using Qwen3TTSModel`

`├── get_text_sentiment.py      # NLP pipeline for emotion classification`

`├── static/output.wav             # The generated audio file served to the frontend`

`└── templates/index.html             # The frontend user interface`

## Models Used

https://huggingface.co/j-hartmann/emotion-english-distilroberta-base
https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice