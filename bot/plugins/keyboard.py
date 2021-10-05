from telebot import types


class Keyboard:
    """Class keyboard."""

    def __init__(self):
        self.keyboard = types.ReplyKeyboardMarkup(True)

    def remove(self):
        self.keyboard = types.ReplyKeyboardRemove(True)
        return self.keyboard

    def add(self, *args):
        self.keyboard.row(*args)
        return self.keyboard
