from gtts import gTTS
import uuid
import os

def text_to_speech(text, lang):
    try:
        if not text.strip():
            text = "Translation completed"

        output_file = f"media/{uuid.uuid4()}.mp3"

        tts = gTTS(text=text, lang=lang)
        tts.save(output_file)

        # debug
        print("Audio generated:", output_file)

        return output_file

    except Exception as e:
        print("TTS ERROR:", str(e))
        return ""