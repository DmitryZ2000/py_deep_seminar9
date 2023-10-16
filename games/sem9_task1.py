# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.


def my_fun(enigma: int, num_try: int):
        # for _ in range(num_try):
    print(enigma)
    enigma = 25
    def new_fun():
        for _ in range(num_try):
            my_answer = int(input('Введите число:  '))
            if my_answer > enigma:
                print('Меньше')
            elif my_answer < enigma:
                print('Больше')
            else:
                print('Верно')
                break
    return new_fun
    


if __name__ == '__main__':

    hello = my_fun(30, 7)
    # print(hello)
    hello()
