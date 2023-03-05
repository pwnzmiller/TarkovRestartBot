import subprocess

from telebot import types

from config import bot


@bot.message_handler(commands=["restart"])
def restart_tarkov_bot(message: types.Message):

    subprocess.Popen(["./script.sh"], shell=False)

    bot.reply_to(message, 'Рестарт выполнен')


if __name__ == '__main__':
    bot.infinity_polling()

