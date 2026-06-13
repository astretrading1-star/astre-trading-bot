import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⭐ Rejoindre le VIP", url="https://t.me/+8DK58OC8UJVkZDFk")],
        [InlineKeyboardButton("👥 Groupe Gratuit", url="https://t.me/astretrading")],
        [InlineKeyboardButton("📞 Support", url="https://t.me/Astre971")]
    ]

    await update.message.reply_text(
        "🔥 BIENVENUE CHEZ ASTRE TRADING 🔥",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
