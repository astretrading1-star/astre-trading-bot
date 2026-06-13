import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_name = update.effective_user.first_name
    
    keyboard = [
        [InlineKeyboardButton("⭐ Rejoindre le Groupe VIP Payant", url="https://t.me/+8DK58OC8UJVkZDFk")],
        [InlineKeyboardButton("👥 Groupe Gratuit", url="https://t.me/astretrading")],
        [InlineKeyboardButton("📞 Support", url="https://t.me/Astre971")]
    ]

    await update.message.reply_text(
    f"🔥 BIENVENUE {user_name} CHEZ ASTRE TRADING 🔥\n\n"
    "📈 Signaux Forex Premium\n"
    "₿ Opportunités Crypto\n"
    "📊 Analyses de marché\n"
    "🎓 Formation Trading\n"
    "⭐ Communauté VIP\n\n"
    "Notre objectif est de vous aider à developper vos compétences et à trader avec discipline.\n\n"
    "🚀 Bon trading et bienvenue dans la communauté Astre Trading\n\n"
    "👇 Choisissez une option ci-dessous :",
    reply_markup=InlineKeyboardMarkup(keyboard)
)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
