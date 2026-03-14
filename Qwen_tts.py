import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel
from get_text_sentiment import top_text_sentiment

def get_audio(textString: str, instruction:str):
    model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
    device_map="cpu",
    dtype=torch.bfloat16
    )
        
    instructions=top_text_sentiment(textString=textString)
    instructions.append(instruction)

    delimiter = ', '
    final_instruction = delimiter.join(instructions)

    wavs, sr = model.generate_custom_voice(
    text=textString,
    language="English",
    speaker="Aiden",
    instruct=final_instruction
    )
    sf.write("static/output.wav", wavs[0], sr)
