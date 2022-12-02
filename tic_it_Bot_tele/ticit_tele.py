from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from qr_generate import createqr

with open("token.txt") as token_file:
    token = token_file.read()

updater = Updater(token,
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/qr - To generate QR code""")


def qr_generate(update: Update, context: CallbackContext):
    received_text = update.message.text.replace("/qr ", "")
    print(received_text)

    createqr(text = received_text)
    update.message.bot.send_photo(update.message.chat.id,open("ticit_QR.png",'rb'))


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

def tele_main():
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('qr', qr_generate))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.command, unknown))  # Filters out unknown commands

    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    updater.start_polling()

