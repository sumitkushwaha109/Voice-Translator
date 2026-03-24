import argostranslate.translate

def translate_text(text, source, target):
    try:
        installed_languages = argostranslate.translate.get_installed_languages()

        from_lang = None
        to_lang = None

        for lang in installed_languages:
            if lang.code == source:
                from_lang = lang
            if lang.code == target:
                to_lang = lang

        if from_lang is None or to_lang is None:
            return "Language not installed"

        translation = from_lang.get_translation(to_lang)

        return translation.translate(text)

    except Exception as e:
        return f"Translation Error: {str(e)}"