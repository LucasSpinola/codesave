from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from nlp import *
import logging
from logs import *

app = FastAPI()

class Pergunta(BaseModel): 
    mensagem: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/pergunta")
def fazer_perguntas(pergunta: Pergunta):
    user_respostas = pergunta.mensagem
    resposta = nlp(user_respostas)

    if resposta == "Infelizmente não encontrei nenhuma resposta para sua pergunta!":    
        log = logging.getLogger(guardar_log())
        log.info({pergunta.mensagem})

    return(resposta)
