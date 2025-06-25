import logging
import os

import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7225094617:AAHY3aLYmIiwLZKcGXx9em3ULK7eviko1NU"
openai.api_key = os.getenv("OPENAI_API_KEY")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I'm a simple bot. Send me any text and I'll echo it back.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reply with an AI-generated answer using OpenAI."""
    question = " ".join(context.args)
    if not question:
        await update.message.reply_text("Please provide a question after /ask.")
        return
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
        )
        answer = response["choices"][0]["message"]["content"].strip()
    except Exception as exc:
        logging.error("OpenAI request failed: %s", exc)
        answer = "Sorry, I couldn't generate a response."
    await update.message.reply_text(answer)

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    app.run_polling()

if __name__ == "__main__":
    main()
