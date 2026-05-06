from telegram.ext import ApplicationBuilder, CommandHandler

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

async def start(update, context):
    await update.message.reply_text("Bot is working!")

app.add_handler(CommandHandler("start", start))

app.run_polling()
