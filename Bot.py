from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

hoy = datetime.now().strftime("%d de %B de %Y")
import random
import os

TOKEN = os.environ["BOT_TOKEN"]

picks = """
🔥 PICKS DEL DÍA

⚽ Fútbol
1️⃣ Inter gana
2️⃣ Over 2.5 Atalanta

🎾 Tenis
3️⃣ Alcaraz gana 2-0

🏀 Basket
4️⃣ Celtics gana
5️⃣ Over 221 Lakers

Stake recomendado
1 = 5€
2 = 10€
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot activo ⚽")

async def picks_today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(picks)

async def daily_picks(context: ContextTypes.DEFAULT_TYPE):
    for chat_id in context.bot_data.get("subscribers", []):
        await context.bot.send_message(chat_id=chat_id, text=picks)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    subs = context.bot_data.setdefault("subscribers", [])
    if chat_id not in subs:
        subs.append(chat_id)
    await update.message.reply_text("Te enviaré las picks cada día a las 09:00.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", subscribe))
app.add_handler(CommandHandler("picks", picks_today))

job_queue = app.job_queue
job_queue.run_daily(daily_picks, time=time(9,0))

app.run_polling()
