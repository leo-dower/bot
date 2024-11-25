import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Fetch the token from the environment variables
token = os.getenv("TELEGRAM_TOKEN")

# Function to respond to /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🎉 Welcome to the *Festa MC - 5 Years* bot! 🎈\n"
        "Available commands:\n"
        "- /info: Details about the party\n"
        "- /local: Event address\n"
        "- /horario: Party schedule\n"
        "- /confirmar: Confirm your attendance."
    )

# Function to provide event details
def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🎊 The party will be on *10/12*, at *6 PM*. Theme: *Night of Glamour*. 💃🕺")

# Function to provide event location
def local(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("📍 *Address:* XYZ Party Hall, 123 Flowers Street, Downtown.")

# Function to provide party schedule
def horario(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("⏰ *Schedule:* The party starts at 6 PM and ends at midnight.")

# Function to confirm attendance
def confirmar(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🎉 Thanks for confirming! Please send your full name to register. 😊")

# Function for unknown commands
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("❓ Sorry, I didn't understand. Please use one of the available commands.")

def main():
    # Create the Updater and pass the bot token
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Adding command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("local", local))
    dispatcher.add_handler(CommandHandler("horario", horario))
    dispatcher.add_handler(CommandHandler("confirmar", confirmar))

    # Adding handler for unknown commands
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
