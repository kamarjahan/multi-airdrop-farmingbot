from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# In-memory storage for user data (this will reset every time the bot restarts)
user_data = {}

def get_user_data(user_id):
    if user_id not in user_data:
        user_data[user_id] = {
            "balance": 0.0,
            "referrals": 0
        }
    return user_data[user_id]

def add_referral(referrer_id, referred_user):
    referrer_data = get_user_data(referrer_id)
    referrer_data["referrals"] += 1
    
    # For every 5 referrals, add 0.1 TON to the referrer's balance
    if referrer_data["referrals"] % 5 == 0:
        referrer_data["balance"] += 0.1





@Client.on_message(filters.command("refer"))
async def refer(client, message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)
    
    me = await client.get_me()  # Get bot details
    referral_link = f"https://t.me/{me.username}?start={user_id}"
    
    # Prepare response text
    response_text = (
        f"Your referral link: {referral_link}\n"
        f"Balance: {user_data['balance']} TON\n"
        f"Referred Persons: {user_data['referrals']}"
    )
    
    # Referral button
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Refer a Friend", url=referral_link)]
    ])
    
    await message.reply_text(response_text, reply_markup=keyboard)
