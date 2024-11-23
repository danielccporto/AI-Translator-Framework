# Data-Driven Translator Project

## Descrição

Este projeto é um sistema de tradução e interação baseado em FastAPI, integrando tecnologias como LangChain, OpenAI, e HuggingFace. Ele oferece múltiplas funcionalidades de tradução e um chatbot para simular interações.

### Funcionalidades
1. Tradução de textos do inglês para francês usando a API da OpenAI.
2. Tradução de textos do inglês para o alemão usando o modelo HuggingFace Helsinki-NLP/opus-mt-en-de.
3. Um chatbot básico utilizando o FakeLLM para responder perguntas predefinidas.

#### Configuração do Ambiente
1. Clonar Repositório 
- git clone <URL_DO_REPOSITORIO>
- cd <NOME_DO_DIRETORIO>

2. Criar Ambiente 
- python -m venv venv
- source venv/bin/activate   # Linux/Mac
- venv\Scripts\activate      # Windows

3. Instalar Dependências 
- pip install -r requirements.txt

4. Configurar Variáveis de Ambiente
- Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
OPENAI_API_KEY=<SUA_API_KEY_OPENAI>
HF_HUB_DISABLE_SYMLINKS_WARNING=1

*Substitua <SUA_API_KEY_OPENAI> pela sua chave de API da OpenAI.

#### Uso 
1. Iniciar o Servidor
- uvicorn app.main:app --reload

2. Acessar a Interface Swagger
- Abra o navegador e acesse http://127.0.0.1:8000/docs para explorar os endpoints.

#### Endpoints Disponíveis
- Rota: /chat
- Método: POST
- Corpo da Solicitação (JSON)

#### Testes 
Os testes estão localizados na pasta tests/ e podem ser executados usando o pytest:
- pytest

#### Dependências
As principais bibliotecas utilizadas no projeto incluem:

fastapi
uvicorn
langchain
transformers
sacremoses
pytest
python-dotenv
Certifique-se de que todas estão instaladas via requirements.txt.


