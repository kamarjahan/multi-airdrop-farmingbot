# plugins/help.py

from pyrogram import Client, filters

@app.on_message(filters.command("help"))
async def help(client, message):
    help_text = (
        "Here is how you can use this bot:\n"
        "- `/start`: Start the bot and see the main menu.\n"
        "- `/refer`: Get your referral link to share with others.\n"
        "- `/help`: Show this help message."
    )
    await message.reply_text(help_text)
