import requests
import telebot
import os
import tempfile

from speech_to_text import speech_to_text
from summary_with_openai import summary_with_davinci

API_TOKEN = "YOUR_TELEGRAM_TOKEN"


def start_bot():
    bot = telebot.TeleBot(API_TOKEN)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.send_message(message.chat.id, "Hi! Send me an audio and I will summarize it for you")

    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
        if not file:
            return "bad request"
        with tempfile.TemporaryDirectory() as tmpdirname:
            bot.send_message(message.chat.id, "Summarizing the audio...")
            audio_path = tmpdirname + file_id + ".oga"
            with open(audio_path, 'wb') as audio_file:
                audio_file.write(file.content)
            transcription = speech_to_text(audio_path)
            summary = summary_with_davinci(transcription)
            bot.send_message(message.chat.id, summary)
            os.remove(audio_path)

    bot.infinity_polling()
