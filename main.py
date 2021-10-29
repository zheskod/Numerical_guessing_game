from random import *

num = randint(1, 100)

print('Добро пожаловать в числовую угадайку')

# функиция проверки числа на принадлежность его к числу и к нашему диапозону (1-100)
def is_valid(input_number):
    flag = False
    if input_number.isdigit():
        if 0 <= int(input_number) <= 100:
            flag = True
    return flag

left = 1
right = 100
correct_number = False

while correct_number == False:
    user_number = input('Введите число от 1 до 100 (включительно): ')
    is_valid(user_number)  # Отправляем введённое число на проверку в функцию
    if is_valid(user_number) == True:  # Если проверку прошла
        user_number = int(user_number)  # преобразуем в целочисленное
        user_name = (left + right) // 2
        if user_number < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif user_number > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        else:
            correct_number = True
            print('Вы угадали, поздравляем!')
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue  # если не прошел условий функций, отправляем еще запрос

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
