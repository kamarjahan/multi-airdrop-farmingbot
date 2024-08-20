# bot.py

from pyrogram import Client
import config

app = Client(
    "crypto_airdrop_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    app.run()
