from app.openai_translator import OpenAITranslator
import pytest

def test_translation():
    translator = OpenAITranslator()
    
    # Testa a tradução de um texto simples
    result = translator.translate("Hello, how are you?")
    assert "Bonjour" in result

    # Testa a tradução de outro texto
    result = translator.translate("What is your name?")
    assert "Comment" in result
