from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Mega download", callback_data='mega_download')],
        [InlineKeyboardButton("Download App", callback_data='download_app')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'mega_download':
        query.edit_message_text(text="How to download from megaz with fastest speed: https://www.youtube.com/watch?v=...")
    elif query.data == 'download_app':
        keyboard = [
            [InlineKeyboardButton("Follow Channel 1", url='https://t.me/FREEUdemyPaidCourse79')],
            [InlineKeyboardButton("Follow Channel 2", url='https://t.me/NetflixCookieOfficial')],
            [InlineKeyboardButton("Done", callback_data='done_following')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="With this app you can use unlimited times. Please follow these 2 Telegram channels:", reply_markup=reply_markup)

def done_following(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Thank you for following the channels. Here is the Mega link: https://mega.nz/...")

def main() -> None:
    updater = Updater("6627462794:AAHGHYTQVFex7mVBpaf3dAHtv0BvrGcVHl0")
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CallbackQueryHandler(done_following, pattern='done_following'))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
