import os
import openai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()

# Configuration Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")
index_name = "patriotesn"

if not pinecone_api_key or not pinecone_env:
    raise ValueError("PINECONE_API_KEY or PINECONE_ENV is not defined. It should be.")

pc = Pinecone(api_key=pinecone_api_key, environment=pinecone_env)

# Vérification de l'index existant
existing_indexes = [idx_info["name"] for idx_info in pc.list_indexes()]
if index_name not in existing_indexes:
    raise ValueError(f"Index {index_name} does not exist on Pinecone.")

# Récupération de l'index
index = pc.Index(index_name)

# Configuration OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not defined. It should be")

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

# Création de la chaîne conversationnelle
llm = ChatOpenAI(api_key=openai_api_key)
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.as_retriever(),
    memory=memory
)

app = FastAPI(title="Chatbot Juridique API")

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@app.get("/")
def root():
    return {"message": "Hello from Patriote SN Chatbot API"}

@app.post("/ask", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest):
    user_question = payload.question
    if not user_question.strip():
        raise HTTPException(status_code=400, detail="Invalid question")

    response = conversation_chain({"question": user_question})
    answer = response["answer"]
    return AnswerResponse(answer=answer)
