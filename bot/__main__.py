#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot

from bot import config
from bot.db import schema
from random import randrange
from bot.plugins.keyboard import Keyboard
from bot.plugins import messages

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start_msg(message):
    """
    Greets the user and shows the help.
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, messages.START_MSG, parse_mode="Markdown")


@bot.message_handler(commands=["help"])
@bot.message_handler(func=lambda msg: msg.text == "Помощь")
def help_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id,
        messages.HELP_MSG,
        reply_markup=keyboard.add("Всё понятно"),
        parse_mode="Markdown",
    )


@bot.message_handler(func=lambda msg: msg.text == "Всё понятно")
def great_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id, messages.GREAT_MESSAGE, reply_markup=keyboard.remove()
    )


@bot.message_handler(func=lambda msg: msg.text == "Да")
def ask_msg(message):
    keyboard = Keyboard()

    bot.send_message(
        message.chat.id, messages.ASK_MESSAGE, reply_markup=keyboard.add("Помощь")
    )


@bot.message_handler(commands=["fortune"])
@bot.message_handler(content_types=["text"])
def get_answer(message):
    keyboard = Keyboard()

    answer, warning, question = schema.main(
        randrange(0, 19), randrange(0, 4), randrange(0, 1),
    )

    text = "*{}*".format(answer) + "\n" + warning + "\n" + question

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=keyboard.add("Да", "Помощь"),
        parse_mode="Markdown",
    )


bot.infinity_polling()
