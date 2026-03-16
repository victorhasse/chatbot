import sys
import aiml
import unicodedata
import re


# Efetua uma filtragem no texto de entrada
def filter(text):
    # Normaliza o texto entrado como parâmetro e remove os acentos
    text = unicodedata.normalize("NFKD", text) \
        .encode("ASCII", "ignore") \
        .decode("utf-8")  # fmt: skip
    # Remove pontuação e caracteres especiais
    text = re.sub(r"[^\w\s]", "", text)
    return text


kb = sys.argv[1] if len(sys.argv) > 1 else "brain.xml" # Pega a base AIML entrada por parâmetro
k = aiml.Kernel()  # Inicializa o motor de interpretação AIML
k.learn(kb)  # Insere a base AIML no motor para aprendizado
while True:  # Executa o laço indefinidamente
    message = input("> ")  # Inicializa o prompt do chatbot
    message = filter(message)  # Limpa a mensagem entrada pelo usuário
    response = k.respond(message)  # Envia ao motor e retorna a resposta
    print(response)  # Imprime a resposta

## python3 main.py brain.xml -> para iniciar.