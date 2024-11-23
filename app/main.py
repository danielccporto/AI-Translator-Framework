from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from app.fake_llm import FakeLLM
from app.openai_translator import OpenAITranslator
from app.huggingface_translator import HuggingFaceTranslator
import os

app = FastAPI()


# Modelos para entrada
class UserInput(BaseModel):
    question: str

class TranslationInput(BaseModel):
    text: str

class HuggingFaceTranslationInput(BaseModel):
    text: str

# Instâncias
fake_llm = FakeLLM()
translator = OpenAITranslator()
hf_translator = HuggingFaceTranslator() 

# Define o template de prompt para o FakeLLM
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="{question}"
)

# Cria uma cadeia simples para o FakeLLM
chain = LLMChain(llm=fake_llm, prompt=prompt_template)

@app.post("/chat")
async def chat(input_data: UserInput):
    """
    Endpoint para perguntas ao FakeLLM.
    """
    try:
        response = chain.run({"question": input_data.question})
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no endpoint /chat: {str(e)}")

@app.post("/translate")
async def translate(input_data: TranslationInput):
    """
    Endpoint para traduzir texto de inglês para francês usando OpenAI.
    """
    try:
        translated_text = translator.translate(input_data.text)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no endpoint /translate: {str(e)}")


@app.post("/translate/de")
async def translate_to_german(input_data: HuggingFaceTranslationInput):
    """
    Endpoint para traduzir texto do inglês para o alemão usando HuggingFace.
    """
    try:
        translated_text = hf_translator.translate(input_data.text)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no endpoint /translate/de: {str(e)}")
