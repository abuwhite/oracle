from bot.plugins.keyboard import Keyboard
from telebot import types


def test_keyboard():
    markup = Keyboard()
    markup.add('test')
    json_str = markup.keyboard.to_json()
    assert 'test' in json_str

    markup.remove()
    json_str = markup.keyboard.to_json()
    assert 'test' not in json_str


# def test_KeyboardButtonPollType():
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton('send me a poll', request_poll=types.KeyboardButtonPollType(type='quiz')))
#     json_str = markup.to_json()
#     assert 'request_poll' in json_str
#     assert 'quiz' in json_str