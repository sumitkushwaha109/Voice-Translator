import whisper
import subprocess
import os

model = whisper.load_model("base")

def speech_to_text(audio_path):
    converted_path = f"{audio_path}_converted.wav"

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", audio_path,
        "-ar", "16000",
        "-ac", "1",
        converted_path
    ])

    result = model.transcribe(converted_path, language="en")

    return result.get("text", "")