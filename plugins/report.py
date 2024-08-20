# plugins/report.py

from pyrogram import Client, filters

# Replace with the actual admin user ID
ADMIN_USER_ID = 1444445604  # Replace with the actual admin's Telegram user ID

@Client.on_message(filters.command("report"))
async def report(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please include a message to report.")
        return
    
    report_text = " ".join(message.command[1:])
    user = message.from_user
    report_message = (
        f"🛠 **Bug Report / Feature Request**\n\n"
        f"**From:** {user.first_name} (@{user.username})\n"
        f"**User ID:** {user.id}\n\n"
        f"**Message:**\n{report_text}"
    )
    
    # Send the report to the admin
    try:
        await client.send_message(ADMIN_USER_ID, report_message)
        await message.reply_text("Your report has been sent to the admin. Thank you!")
    except Exception as e:
        await message.reply_text("Failed to send the report. Please try again later.")
        print(f"Error sending report: {e}")
