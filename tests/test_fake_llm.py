import pytest
from app.fake_llm import FakeLLM

def test_fake_llm_call():
    """Teste o método _call diretamente no FakeLLM."""
    fake_llm = FakeLLM()

    # Testa perguntas conhecidas
    assert fake_llm._call("Qual é o seu nome?") == "Eu sou um chatbot fake."
    assert fake_llm._call("Qual é a capital do Brasil?") == "A capital do Brasil é Brasília."
    assert fake_llm._call("Como você está?") == "Eu estou funcionando perfeitamente, obrigado!"

    # Testa uma pergunta desconhecida
    assert fake_llm._call("O que é LangChain?") == "Desculpe, não entendi sua pergunta."

def test_fake_llm_case_insensitive():
    """Teste de insensibilidade a maiúsculas e minúsculas."""
    fake_llm = FakeLLM()

    assert fake_llm._call("qual É o seu nome?") == "Eu sou um chatbot fake."
    assert fake_llm._call("QUAL É A CAPITAL DO BRASIL?") == "A capital do Brasil é Brasília."

def test_fake_llm_with_extra_spaces():
    """Teste para garantir que espaços extras são ignorados."""
    fake_llm = FakeLLM()

    assert fake_llm._call("  Qual é o seu nome?  ") == "Eu sou um chatbot fake."
    assert fake_llm._call("   Qual é a capital do Brasil?   ") == "A capital do Brasil é Brasília."
