#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot

from magipy import config
from magipy.db import schema
from magipy.utils.generate import variant, answer

bot = telebot.TeleBot(config.token)


class Keyboard:
    """Class keyboard"""
    def __init__(self):
        self.keyboard = telebot.types.ReplyKeyboardMarkup(True)

    def generate_btn(self, *args):
        self.keyboard.row(*args)
        return self.keyboard


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Вы задаете вопрос, на который можно ответить «да» или «нет», а шар дает "
        "ответ. Спрашивайте.",
    )


@bot.message_handler(content_types=["text"])
def gen_message(message):

    keyboard = Keyboard()

    if message.text == "Помощь":
        text = "Вы задаёте любой вопрос, на который можно ответить «да», «нет» или «может быть», а шар вам отвечает."
        bot.send_message(
            message.chat.id, text, reply_markup=keyboard.generate_btn("Всё понятно")
        )
    elif message.text == "Всё понятно":
        text = "Отлично! Задайте свой вопрос."
        bot.send_message(
            message.chat.id, text, reply_markup=keyboard.generate_btn("Помощь")
        )
    elif message.text == "Да":
        text = "Спрашивайте."
        bot.send_message(
            message.chat.id, text, reply_markup=keyboard.generate_btn("Помощь")
        )
    elif message.text:
        variants = schema.VARIANTS[variant()]
        table = schema.get_table(variants)

        answers = table.get(answer())
        text = answers + "\n" + "Ещё вопрос?"

        bot.send_message(
            message.chat.id, text, reply_markup=keyboard.generate_btn("Да", "Помощь")
        )


bot.infinity_polling()
