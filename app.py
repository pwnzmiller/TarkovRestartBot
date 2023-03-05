import subprocess

from telebot import types

from config import bot


@bot.message_handler(commands=["restart"])
def restart_tarkov_bot(message: types.Message):
    try:
        subprocess.Popen(["sh", "docker run hello-world"], shell=False)
    except:
        bot.reply_to(message, 'Ошибка при выполнении рестарта')

    bot.reply_to(message, 'Рестарт выполнен')


if __name__ == '__main__':
    bot.infinity_polling()

