from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# Define conversation states
CHOOSING, FOLLOWING, MEGA_DOWNLOAD = range(3)

# Function to handle /start command
def start(update: Update, _: CallbackContext) -> int:
    keyboard = [
        [InlineKeyboardButton("Mega download", callback_data=str(CHOOSING))],
        [InlineKeyboardButton("Download App", callback_data=str(FOLLOWING))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Chào mừng bạn đến với Bot của chúng tôi! Vui lòng chọn một chức năng:",
        reply_markup=reply_markup,
    )
    return CHOOSING

# Function to handle 'Mega download' button press
def mega_download(update: Update, _: CallbackContext) -> int:
    update.callback_query.answer()
    update.callback_query.message.reply_text(
        "Để tải về từ Mega với tốc độ nhanh nhất, hãy truy cập vào đường link YouTube sau đây: <your_youtube_link>"
    )
    return ConversationHandler.END

# Function to handle 'Download App' button press
def download_app(update: Update, _: CallbackContext) -> int:
    update.callback_query.answer()
    keyboard = [
        [InlineKeyboardButton("Follow Channel 1", url="https://t.me/FREEUdemyPaidCourse79'")],
        [InlineKeyboardButton("Follow Channel 2", url="https://t.me/NetflixCookieOfficial'")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.reply_text(
        "Vui lòng theo dõi cả hai kênh Telegram sau để nhận được liên kết Mega download:",
        reply_markup=reply_markup,
    )
    return FOLLOWING

# Function to handle user following both channels
def following(update: Update, _: CallbackContext) -> int:
    update.callback_query.answer()
    update.callback_query.message.reply_text(
        "Chúc mừng! Bạn đã follow thành công cả hai kênh Telegram. Bây giờ bạn có thể nhận liên kết Mega download: <your_mega_link>"
    )
    return ConversationHandler.END

# Function to handle user input that is not a button
def fallback(update: Update, _: CallbackContext):
    update.message.reply_text("Vui lòng chọn một trong các chức năng trên.")

def main():
    # Replace 'YOUR_TOKEN' with your actual Telegram Bot token
    updater = Updater("6627462794:AAHGHYTQVFex7mVBpaf3dAHtv0BvrGcVHl0")
    dispatcher = updater.dispatcher

    # Define conversation handler for /start command
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                CallbackQueryHandler(mega_download, pattern='^' + str(CHOOSING) + '$'),
                CallbackQueryHandler(download_app, pattern='^' + str(FOLLOWING) + '$'),
            ],
            FOLLOWING: [
                CallbackQueryHandler(following, pattern='^' + str(FOLLOWING) + '$'),
            ],
        },
        fallbacks=[],
    )

    # Add the conversation handler to the dispatcher
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, fallback))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
