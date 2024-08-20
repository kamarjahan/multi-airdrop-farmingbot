# plugins/start.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

@app.on_message(filters.command("start"))
async def start(client, message):
    # Replace this with the path to your image or a URL
    image_url = "https://futrengine.github.io/images/youtube-logo.png"
    text = (
        "THIS BOT IS USED FOR FARMING CRYPTO AIRDROP IN ALL IN ONE BOT WITH TRUSTABLE CRYPTOS MINI APP.\n"
        "THIS BOT IS ONLY FOR MANAGING YOUR ALL AIRDROP FARM IN SINGLE PLACE FOR SIMPLICITY.\n"
        "THIS BOT HAS ALL TRUSTABLE AND TOP AIRDROP PROJECT MINI APPS AND SITES."
    )
    
    # Inline buttons
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Catizen", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Mini App 2", url="https://miniapp2.example.com"),
            InlineKeyboardButton("Mini App 3", url="https://miniapp3.example.com"),
            InlineKeyboardButton("Mini App 4", url="https://miniapp4.example.com"),
            InlineKeyboardButton("Mini App 5", url="https://miniapp5.example.com")
        ],
        [
            InlineKeyboardButton("Chick Coop", url="https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1444445604"),
            InlineKeyboardButton("Mini App 7", url="https://miniapp7.example.com"),
            InlineKeyboardButton("Mini App 8", url="https://miniapp8.example.com"),
            InlineKeyboardButton("Mini App 9", url="https://miniapp9.example.com"),
            InlineKeyboardButton("Mini App 10", url="https://miniapp10.example.com")
        ]
    ])

    # Send photo with caption and buttons
    await message.reply_photo(
        photo=image_url,
        caption=text,
        reply_markup=keyboard
    )
