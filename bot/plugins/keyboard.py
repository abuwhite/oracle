import telebot


class Keyboard:
    """Class keyboard."""

    def __init__(self):
        self.keyboard = telebot.types.ReplyKeyboardMarkup(True)

    def remove(self):
        self.keyboard = telebot.types.ReplyKeyboardRemove(True)
        return self.keyboard

    def add(self, *args):
        self.keyboard.row(*args)
        return self.keyboard
