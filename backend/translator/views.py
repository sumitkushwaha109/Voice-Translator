from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from django.conf import settings
from .services.speech_to_text import speech_to_text
from .services.translate import translate_text
from .services.text_to_speech import text_to_speech

@api_view(['POST'])
def translate_voice(request):
    audio = request.FILES['audio']
    input_lang = request.data.get('input_lang')
    output_lang = request.data.get('output_lang')

    file_path = os.path.join(settings.MEDIA_ROOT, audio.name)
    print("Saved file:", file_path)

    with open(file_path, 'wb') as f:
        for chunk in audio.chunks():
            f.write(chunk)

    text = speech_to_text(file_path)
    print("Detected Text:", text)

    translated = translate_text(text, input_lang, output_lang)

    audio_file = text_to_speech(translated, output_lang)

    return Response({
        "input_text": text,
        "translated_text": translated,
        "audio_url": audio_file
    })