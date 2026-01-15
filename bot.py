import asyncio
import random
from datetime import datetime, timedelta
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread
import os

# Telegram Token ve Chat ID
TOKEN = os.getenv("BOT_TOKEN")  # Railway secrets kullan
CHAT_ID = int(os.getenv("CHAT_ID"))  # Railway secrets kullan

bot = Bot(token=TOKEN)

emoji_sets = [
    "💸💯👑",
    "✨💵🎉",
    "💎🤑🔥",
    "💰💎💯"
]

# Flask web server (Railway için keep-alive)
app = Flask('')

@app.route('/')
def home():
    return "Bot aktif 🚀"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# /start komutu için async fonksiyon
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emojiler = random.choice(emoji_sets)
    mesaj = f"<b>{emojiler} —GÜN SONU— {emojiler}</b>"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mesaj, parse_mode='HTML')
    print("Test mesajı /start ile gönderildi")

# Gün sonu mesajı için async fonksiyon
async def daily_message():
    while True:
        now = datetime.now()
        # Gelecek günün 23:59 zamanı
        next_run = now.replace(hour=23, minute=59, second=0, microsecond=0)
        if now >= next_run:
            next_run += timedelta(days=1)
        
        wait_seconds = (next_run - now).total_seconds()
        await asyncio.sleep(wait_seconds)  # Tam 23:59’a kadar bekle

        emojiler = random.choice(emoji_sets)
        mesaj = f"<b>{emojiler} —GÜN SONU— {emojiler}</b>"
        await bot.send_message(chat_id=CHAT_ID, text=mesaj, parse_mode='HTML')
        print(f"Gün sonu mesajı gönderildi: {mesaj}")

# Botu başlat
async def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    
    # Gün sonu mesajını paralel çalıştır
    asyncio.create_task(daily_message())
    
    print("Bot başladı 😎")
    await app_bot.run_polling()

asyncio.run(main())
