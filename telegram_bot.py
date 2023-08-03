from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot token
BOT_TOKEN = '6627462794:AAHGHYTQVFex7mVBpaf3dAHtv0BvrGcVHl0'
CHANNEL_LINK_1 = 'https://t.me/FREEUdemyPaidCourse79'
CHANNEL_LINK_2 = 'https://t.me/NetflixCookieOfficial'
MEGA_LINK = 'https://mega.nz/'

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Mega download", callback_data='mega')],
        [InlineKeyboardButton("Download App", callback_data='app')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Bot functions:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    if query.data == 'mega':
        query.message.reply_text('How to download from mega with fastest speed: ' + MEGA_LINK)
    elif query.data == 'app':
        keyboard = [
            [InlineKeyboardButton("Follow Channel 1", url=CHANNEL_LINK_1)],
            [InlineKeyboardButton("Follow Channel 2", url=CHANNEL_LINK_2)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text('Follow the channels to unlock the Download App link:', reply_markup=reply_markup)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
              