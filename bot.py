from pyrogram import Client, idle

# Import your plugins
from plugins import start, refer, report

# Configuration
API_ID = '17875613'
API_HASH = '6798f54a7f74e94f2ef0923fba8a8377'
BOT_TOKEN = '7513524486:AAFlIPgdbEsui9DNmTqAXTzQr1t37O_E6vc'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    app.start()
    print("Bot is running!")
    idle()  # Keep the bot running
    app.stop()
