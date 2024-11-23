from app.huggingface_translator import HuggingFaceTranslator

def test_huggingface_translation():
    translator = HuggingFaceTranslator()
    text = "Good morning!"
    translated = translator.translate(text)
    assert "Guten Morgen" in translated
