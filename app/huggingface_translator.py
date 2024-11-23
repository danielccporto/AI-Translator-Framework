from transformers import pipeline

class HuggingFaceTranslator:
    """
    Classe para traduzir texto do inglês para o alemão usando HuggingFace diretamente.
    """
    def __init__(self):
        # Carrega o modelo pré-treinado da HuggingFace
        self.model_pipeline = pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-de"
        )

    def translate(self, text: str) -> str:
        """
        Traduz o texto do inglês para o alemão.

        Args:
            text (str): Texto em inglês.

        Returns:
            str: Texto traduzido para o alemão.
        """
        # Realiza a tradução diretamente usando o pipeline
        translation = self.model_pipeline(text)
        return translation[0]['translation_text']
