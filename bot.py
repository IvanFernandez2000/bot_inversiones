
from flask import Flask, request
from telegram import Bot
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder al token desde la variable de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    bot.send_message(chat_id, '¡Hola! Bot en funcionamiento.')
    return 'OK'

if __name__ == '__main__':
    app.run(port=5000)