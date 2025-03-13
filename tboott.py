from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# دریافت توکن از متغیر محیطی
TOKEN = "7664721856:AAEIsH8nspc_1UmLwgu3CLEFErbAgI3Fgoc"

# دستور /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من یه بات حل‌کننده معادلات ریاضی هستم. یه معادله بفرست تا جوابش رو بگم.")

# حل معادلات ریاضی
def solve_math(update: Update, context: CallbackContext):
    try:
        expression = update.message.text  # گرفتن متن پیام
        result = eval(expression)  # محاسبه مقدار عبارت
        update.message.reply_text(f"🔢 جواب: {result}")
    except:
        update.message.reply_text("❌ معادله نامعتبره! لطفاً یه عبارت درست بفرست.")

# راه‌اندازی بات
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, solve_math))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
