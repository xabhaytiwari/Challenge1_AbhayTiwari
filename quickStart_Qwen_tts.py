import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel
from get_text_sentiment import top_text_sentiment

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign",
    device_map="cpu",
    dtype=torch.bfloat16
)

textString = "You have got the job! yay!"
wavs, sr = model.generate_voice_design(
    text=textString,
    language="English",
    instruct=top_text_sentiment(textString=textString)
)

sf.write("output_voice_design.wav", wavs[0], sr)