# plugins/start.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

@Client.on_message(filters.command("start"))
async def start(client, message):
    args = message.text.split()
    referred_by = None

    if len(args) > 1:
        referred_by = int(args[1])
        referrer_data = get_user_data(referred_by)

        # Notify the referrer
        try:
            referrer_message = (
                f"You have successfully referred {message.from_user.first_name} (@{message.from_user.username})!"
            )
            await client.send_message(referred_by, referrer_message)

            # Add the referral to the referrer
            add_referral(referred_by, message.from_user.id)
        except Exception as e:
            print(f"Failed to notify referrer: {e}")

    # Usual start message
    image_url = "https://telegra.ph/file/9e2dac29b8fb7f1808b42.jpg"
    text = (
        "THIS BOT IS USED FOR FARMING CRYPTO AIRDROP IN ALL IN ONE BOT WITH TRUSTABLE CRYPTOS MINI APP.\n"
        "THIS BOT IS ONLY FOR MANAGING YOUR ALL AIRDROP FARM IN SINGLE PLACE FOR SIMPLICITY.\n"
        "THIS BOT HAS ALL TRUSTABLE AND TOP AIRDROP PROJECT MINI APPS AND SITES."
    )
    
    # Inline buttons
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Catizen", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Chick Coop", url="https://t.me/chickcoopofficial_bot/chickcoop?startapp=ref_1444445604")
        ],
        [
            InlineKeyboardButton("Hamster Kombat", url="https://t.me/upcoming"),
            InlineKeyboardButton("Simple Coin", url="https://miniapp10.example.com")
        ],
        [
            InlineKeyboardButton("Cex.io", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Memefi Coin", url="https://miniapp2.example.com")
        ],
        [
            InlineKeyboardButton("w-coin", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Vertus", url="https://miniapp2.example.com")
        ],
        [
            InlineKeyboardButton("b-coin 2048", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Time Farm", url="https://t.me/TimeFarmCryptoBot?start=nywnmeq5oNl8KgW0")
        ],
        [
            InlineKeyboardButton("Yes Coin", url="https://t.me/theYescoin_bot/Yescoin?startapp=lVDUJa"),
            InlineKeyboardButton("Banana", url="https://t.me/OfficialBananaBot/banana?startapp=referral=4DVG1B1")
        ],
        [
            InlineKeyboardButton("Eden", url="https://t.me/Edencoin_bot?start=ref_916697"),
            InlineKeyboardButton("Seed App", url="https://t.me/seed_coin_bot/app?startapp=1444445604")
        ],
        [
            InlineKeyboardButton("Dormint", url="https://t.me/catizenbot/gameapp?startapp=r_1312_25992402"),
            InlineKeyboardButton("Dogs", url="https://t.me/dogshouse_bot/join?startapp=jBTqXxHAQAOTwEszaG3xvA")
        ],
        [
            InlineKeyboardButton("Blum", url="https://t.me/BlumCryptoBot/app?startapp=ref_XCqlJxp1eE"),
            InlineKeyboardButton("X empire", url="https://miniapp2.example.com")
        ]
    ])

    # Send photo with caption and buttons
    await message.reply_photo(
        photo=image_url,
        caption=text,
        reply_markup=keyboard
    )
