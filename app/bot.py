from flask import Flask, request, jsonify
from telegram import Bot
from dotenv import load_dotenv
import os
import asyncio
from app.models.database import init_db

# Inicializa las tablas al iniciar la aplicación
init_db()

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route('/', methods=['POST'])
def webhook():
    if request.is_json:  # Verificar si la solicitud es JSON
        update = request.get_json()  # Leer el JSON
        print(update)  # Verificar en consola
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            asyncio.run(bot.send_message(chat_id, '¡Hola! Bot en funcionamiento.'))
        return jsonify({'status': 'OK'}), 200  # Respuesta JSON

    return jsonify({'error': 'Unsupported Media Type'}), 415  # Error si no es JSON

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)