# plugins/refer.py

from pyrogram import Client, filters

@app.on_message(filters.command("refer"))
async def refer(client, message):
    referral_link = f"https://t.me/{client.username}?start={message.from_user.id}"
    await message.reply_text(f"Share this link with others to refer them: {referral_link}")
