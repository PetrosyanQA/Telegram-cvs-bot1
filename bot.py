import os
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from groq import Groq

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

client = Groq(api_key=GROQ_API_KEY)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    file_path = await file.get_file()
    file_name = file.file_name
    await file_path.download_to_drive(file_name)

    df = pd.read_csv(file_name)
    top_products = df.sort_values(by="Sales", ascending=False).head(5)

    response_text = "Топ 5 товаров по продажам:\n"
    for i, row in top_products.iterrows():
        response_text += f"{row['Name']} — Продажи: {row['Sales']}, Цена: {row['Final price']}\n"

    await update.message.reply_text(response_text)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":user_message}]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.Document.FileExtension("csv"), handle_file))
app.add_handler(MessageHandler(filters.TEXT, handle_text))

app.run_polling()
