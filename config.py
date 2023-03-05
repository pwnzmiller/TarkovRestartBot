import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)

users = [182281819, 387340246]