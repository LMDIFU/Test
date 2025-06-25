# Simple Telegram Bot

This repository contains a minimal example of a Telegram bot written in Python using the `python-telegram-bot` library.

## Files

- `simple_bot.py` – a bot that can echo messages and answer questions using OpenAI.

## Usage

1. Install dependencies:
   ```bash
   pip install python-telegram-bot openai
   ```
2. Set your OpenAI API key in the `OPENAI_API_KEY` environment variable.
3. Run the bot:
   ```bash
   python simple_bot.py
   ```

Before running, make sure to set your bot token in `simple_bot.py`.
Use the `/ask` command followed by your question to get an AI-generated response.
