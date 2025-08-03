import telebot
from config import TELEGRAM_BOT_TOKEN
from utils.yandex_speech import synthesize_text
from utils.intent_detector import ask_yandex_gpt

bot = telebot.TeleBot(8217436535:AAEghCWc2y-2leOjxzkJdUnbae88QIqvtXw)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Задай мне вопрос, и я отвечу голосом 🙂")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    question = message.text
    bot.send_message(message.chat.id, f"Ты спросил: {question}")

    # Генерация ответа
    answer = ask_yandex_gpt(question)
    bot.send_message(message.chat.id, f"Ответ: {answer}")

    # Озвучка
    audio_file = synthesize_text(answer)
    with open(audio_file, 'rb') as f:
        bot.send_voice(message.chat.id, f)

bot.polling(none_stop=True)

