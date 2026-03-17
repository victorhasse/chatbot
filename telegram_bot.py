import aiml
import unicodedata
import re
import os
import sys
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv("TOKEN")

def filter_text(text):
    text = unicodedata.normalize("NFKD", text) \
        .encode("ASCII", "ignore") \
        .decode("utf-8")
    text = re.sub(r"[^\w\s]", "", text)
    return text.upper()

kernel = aiml.Kernel()
kernel.learn("brain.xml")

def teclado_menu():
    return ReplyKeyboardMarkup(
        [["1 - Comprar Produto", "2 - Ajuda"]],
        resize_keyboard=True
    )

def teclado_sim_nao():
    return ReplyKeyboardMarkup(
        [["SIM", "NAO"]],
        resize_keyboard=True
    )

def teclado_comprar():
    return ReplyKeyboardMarkup(
        [["JOGOS", "CARRINHO"]],
        resize_keyboard=True
    )

def teclado_jogos():
    return ReplyKeyboardMarkup(
        [["JOGO 1", "JOGO 2", "JOGO 3"],
         ["VOLTAR"]],
        resize_keyboard=True
    )

def teclado_carrinho():
    return ReplyKeyboardMarkup(
        [["PIX", "CARTAO"],
         ["JOGOS", "REMOVER"]],
        resize_keyboard=True
    )

def teclado_pagamento():
    return ReplyKeyboardMarkup(
        [["PAGO", "FALHOU"]],
        resize_keyboard=True
    )

def teclado_ajuda():
    return ReplyKeyboardMarkup(
        [["REEMBOLSO", "ATENDENTE"]],
        resize_keyboard=True
    )

def teclado_vazio():
    return ReplyKeyboardRemove()

def escolher_teclado(resposta):
    resposta = resposta.upper()
    if "COMPRAR PRODUTO" in resposta or "AJUDA" in resposta:
        return teclado_menu()
    if "LOGADO NO APP" in resposta:
        return teclado_sim_nao()
    if "LISTA DE JOGOS" in resposta and "CARRINHO" in resposta:
        return teclado_comprar()
    if "JOGO 1" in resposta:
        return teclado_jogos()
    if "ADICIONAR" in resposta:
        return teclado_sim_nao()
    if "ADICIONADO AO CARRINHO" in resposta or "SEU CARRINHO" in resposta:
        return teclado_carrinho()
    if "PIX" in resposta and "PAGO" in resposta:
        return teclado_pagamento()
    if "REEMBOLSO" in resposta and "ATENDENTE" in resposta:
        return teclado_ajuda()
    if "REEMBOLSAR" in resposta:
        return teclado_sim_nao()
    return teclado_vazio()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resposta = kernel.respond("OLA")
    teclado = escolher_teclado(resposta)
    await update.message.reply_text(resposta, reply_markup=teclado)

async def mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    if texto == "1 - Comprar Produto":
        texto = "MENU 1"
    elif texto == "2 - Ajuda":
        texto = "MENU 2"
    texto_filtrado = filter_text(texto)
    resposta = kernel.respond(texto_filtrado)
    if not resposta:
        resposta = "Desculpe, nao entendi. Digite MENU para voltar ao inicio."
    teclado = escolher_teclado(resposta)
    await update.message.reply_text(resposta, reply_markup=teclado)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensagem))
    print("SigmaBOT rodando no Telegram...")
    try:
        app.run_polling(drop_pending_updates=True)
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    