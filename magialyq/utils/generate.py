from magialyq.api import random


def variant():
    items = random.api.generate_integers(1, 0, 3)
    return next((item for item in items))


def answer():
    items = random.api.generate_integers(1, 0, 4)
    return next((item for item in items))
