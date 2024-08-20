import pyrogram
from pyrogram import filters

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = pyrogram.Client("my_bot", api_id=YOUR_API_ID, api_hash=YOUR_API_HASH, bot_token="YOUR_BOT_TOKEN")

@bot.on_message(filters.command("start"))
async def start(client, message):
    # Code to send a message with inline buttons
    await client.send_message(message.chat.id, "Choose an option:", reply_markup=inline_keyboard)

# Define the inline keyboard
inline_keyboard = [
    [
        pyrogram.InlineKeyboardButton("Open Mini App", web_app=pyrogram.WebAppInfo(url="https://your_mini_app_url"))
    ],
    [
        pyrogram.InlineKeyboardButton("Visit Website", url="https://your_website_url")
    ]
]

bot.run()
