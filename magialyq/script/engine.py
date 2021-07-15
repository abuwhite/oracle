from magialyq.api import config
import telebot
from magialyq.utils import generate, db

bot = telebot.TeleBot(config.token)


def run():
    @bot.message_handler(commands=['start'])
    def start_command(message):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('🔮')

        if message:
            bot.send_message(message.chat.id, 'Что вы хотите узнать у шара?', reply_markup=keyboard)

            @bot.message_handler(content_types=["text"])
            def gen_message(message):
                if message.text not in {'ещё', 'ещё вопрос', 'да'}:
                    variant = db.VARIANTS[generate.variant()]
                    table = db.get_table(variant)

                    answer = table.get(generate.answer())
                    bot.send_message(message.chat.id, answer)

                    quest = 'Если вы хотите узнать что-то ещё, задайте вопрос или нажмите на ' \
                            '"🔮" '
                    bot.send_message(message.chat.id, quest, reply_markup=keyboard)

    bot.infinity_polling()
