from random import randint


def throw_dice(number):
    return [randint(1, 6) for _ in range(number)]
