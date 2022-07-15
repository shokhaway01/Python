import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "AAGI0ddcb2KW5HEF9fCED4vEAieA5pBmOgw"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )
    xabar = f"Ну здравствуй тварь, {username} Хочешь переводить лотынь на кирилицу"
    xabar += "\Отправь мне любое слово и текст!."
    bot.reply_to(message, xabar)



@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()
