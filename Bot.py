from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

TOKEN = os.environ["BOT_TOKEN"]

picks = [
    "Real Madrid gana",
    "Más de 2.5 goles",
    "Ambos marcan",
    "Barcelona gana",
    "Empate al descanso"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot activo ⚽")

async def pick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(picks))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pick", pick))

app.run_polling()
