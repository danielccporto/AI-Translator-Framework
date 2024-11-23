from langchain.llms.base import LLM
from typing import Optional

class FakeLLM(LLM):
    """
    FakeLLM para simular um modelo de linguagem com respostas pré-definidas.
    """

    @property
    def _llm_type(self) -> str:
        return "fake_llm"

    def _call(self, prompt: str, stop: Optional[str] = None) -> str:
        """
        Retorna uma resposta com base no prompt fornecido.
        """
        # Debug para verificar o prompt recebido
        print(f"Prompt recebido: '{prompt}'")

        # Normaliza o prompt
        prompt = prompt.strip()

        # Respostas pré-definidas
        respostas = {
            "qual é o seu nome?": "Eu sou um chatbot fake.",
            "qual é a capital do brasil?": "A capital do Brasil é Brasília.",
            "como você está?": "Eu estou funcionando perfeitamente, obrigado!"
        }

        # Retorna a resposta correspondente ou uma mensagem padrão
        resposta = respostas.get(prompt.lower(), "Desculpe, não entendi sua pergunta.")

        # Debug para verificar a resposta gerada
        print(f"Resposta gerada: '{resposta}'")
        return resposta
