# Telegram CSV + Groq Bot

Этот бот для Telegram умеет:

- Принимать CSV-файлы и анализировать топ-продукты по продажам
- Отвечать на текстовые сообщения через Groq AI

## Установка и запуск

1. Создать Telegram бота через [BotFather](https://t.me/BotFather) и получить `TELEGRAM_TOKEN`
2. Получить `GROQ_API_KEY` на [Groq](https://groq.ai)
3. В корне репозитория должны быть файлы:
   - `bot.py`
   - `requirements.txt`
   - `.gitignore`
   - `README.md`
4. На Render:
   - Создать Web Service → подключить репозиторий
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
   - Добавить Environment Variables:
     - `TELEGRAM_TOKEN`
     - `GROQ_API_KEY`
5. Deploy → бот будет работать 24/7

## Примечания

- Файл `bot.py` должен быть в корне репозит# 
