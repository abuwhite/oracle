#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot

from bot.config import Config, Messages
from bot.db import schema
from random import randrange


bot = telebot.TeleBot(Config.BOT_TOKEN)


class Keyboard:
    """Class keyboard"""

    def __init__(self):
        self.keyboard = telebot.types.ReplyKeyboardMarkup(True)

    def clean(self):
        self.keyboard = telebot.types.ReplyKeyboardRemove(True)
        return self.keyboard

    def add_btn(self, *args):
        self.keyboard.row(*args)
        return self.keyboard


@bot.message_handler(commands=["start"])
def start_msg(message):
    bot.send_message(
        message.chat.id,
        Messages.START_MSG,
        parse_mode='Markdown'
    )


@bot.message_handler(commands=["help"])
@bot.message_handler(func=lambda msg: msg.text == 'Помощь')
def help_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id, Messages.HELP_MSG,
        reply_markup=keyboard.add_btn("Всё понятно"),
        parse_mode='Markdown'
    )


@bot.message_handler(func=lambda msg: msg.text == 'Всё понятно')
def great_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id,
        Messages.GREAT_MESSAGE,
        reply_markup=keyboard.clean()
    )


@bot.message_handler(func=lambda msg: msg.text == 'Да')
def ask_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id, Messages.ASK_MESSAGE,
        reply_markup=keyboard.add_btn("Помощь")
    )


@bot.message_handler(content_types=["text"])
def get_answer(message):
    keyboard = Keyboard()

    answer, warning, question = schema.main(
        randrange(0, 19),
        randrange(0, 4),
        randrange(0, 1)
    )

    text = answer + "\n" + warning + "\n" + question

    bot.send_message(
        message.chat.id, text,
        reply_markup=keyboard.add_btn("Да", "Помощь")
    )


bot.infinity_polling()
