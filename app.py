import subprocess

from telebot import types

from config import bot


@bot.message_handler(commands=["restart"])
def restart_tarkov_bot(message: types.Message):
    LINE = ''

    proc = subprocess.Popen(["sh", "script.sh"], shell=False, stdout=subprocess.PIPE)

    output = proc.stdout.read()

    bot.reply_to(message, output)


if __name__ == '__main__':
    bot.infinity_polling()

