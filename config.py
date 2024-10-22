from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')
DATABASE_URI = os.getenv('DATABASE_URI')
DEBUG = 'TURE'

