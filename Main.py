
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your own bot token
BOT_TOKEN = "7725560869:AAGrWT59IZdP_JvmgLdbnwVd-uVE-gdq2x4"
# Channel link to be joined
CHANNEL_LINK = "https://t.me/spike_gamerz1"
# Link to the file you want to share
FILE_LINK = "https://t.me/spike_gamerz1/347"  

def start(update: Update, context: CallbackContext) -> None:
    # Send a welcome message and prompt to join the channel
    update.message.reply_text(
        f"Hello! To access the file, please join our channel: {https://t.me/animesagaxhub} \n\nUse /join_channel to check your membership."
    )

def join_channel(update: Update, context: CallbackContext) -> None:
    # Check if the user is a member of the channel
    user_id = update.message.from_user.id
    chat_member = context.bot.get_chat_member(chat_id="@spike_gamerz1", user_id=user_id)

    if chat_member.status in ["member", "administrator", "creator"]:
        # If user is a member, send the file link
        update.message.reply_text(f"Thanks for joining! Here is your file link: {FILE_LINK}")
    else:
        # If user is not a member
        update.message.reply_text(f"Please join the channel to get the file.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    # Command handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('join_channel', join_channel))

    # Start the bot
    updater.start_polling()
    updater.idle()  # Keep the bot running until interrupted

if __name__ == '__main__':
    main()
