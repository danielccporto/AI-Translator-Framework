from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

# Certifique-se de configurar sua chave de API da OpenAI
api_key = os.getenv("OPENAI_API_KEY")

class OpenAITranslator:
    """
    Classe para traduzir texto usando o modelo da OpenAI via LangChain.
    """
    def __init__(self):
        self.chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

        # Template para a tradução
        self.prompt_template = PromptTemplate(
            input_variables=["text"],
            template="Translate the following text from English to French:\n\n{text}"
        )

        # Chain de tradução
        self.translation_chain = LLMChain(
            llm=self.chat_model,
            prompt=self.prompt_template
        )

    def translate(self, text: str) -> str:
        """
        Traduz o texto para o francês.

        Args:
            text (str): Texto em inglês.

        Returns:
            str: Texto traduzido para o francês.
        """
        return self.translation_chain.run({"text": text})

