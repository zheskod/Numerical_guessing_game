from random import *

num = randint(1, 100)

print('Добро пожаловать в числовую угадайку')


def is_valid(input_number):
    flag = False
    if input_number.isdigit():
        if 0 <= int(input_number) <= 100:
            flag = True
    return flag
