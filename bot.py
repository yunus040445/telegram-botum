import asyncio
import random
from telegram import Bot
from telegram.constants import ParseMode

TOKEN = "8534122580:AAF6bhd46cnOvT-sgX4iLfYEx_qa12BOEmU"
CHAT_ID = 5452763929

bot = Bot(token=TOKEN)

emoji_sets = [
    "💸💯👑",
    "✨💵🎉",
    "💎🤑🔥",
    "💰💎💯"
]

async def main():
    print("Bot başladı 😎 Her 60 saniyede süslü GÜN SONU mesajı atacak")
    while True:
        emojiler = random.choice(emoji_sets)
        mesaj = f"<b>{emojiler} —GÜN SONU— {emojiler}</b>"
        await bot.send_message(chat_id=CHAT_ID, text=mesaj, parse_mode=ParseMode.HTML)
        await asyncio.sleep(60)

asyncio.run(main())
