import subprocess

from telebot import types

from config import bot, users


@bot.message_handler(commands=["restart"])
def restart_tarkov_bot(message: types.Message):
    if message.from_user.id in users:
        try:
            proc = subprocess.Popen(["sh", "script.sh"], shell=False, stdout=subprocess.PIPE)

            output = proc.stdout.read()

            bot.reply_to(message, output)
        except:
            bot.reply_to(message, "Возникла ошибка")


@bot.message_handler(commands=["ping"])
def ping(message: types.Message):
    bot.reply_to(message, 'pong')


if __name__ == '__main__':
    bot.infinity_polling()

