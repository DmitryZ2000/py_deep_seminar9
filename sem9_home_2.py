# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать
# по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
# Функция принимает два аргумента:

# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения
# вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:

# a, b, c (целые числа) - коэффициенты квадратного уравнения.

# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит
# параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет
# сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

import csv
import json
from random import randint as rnd


def generate_csv_file(file_name:str='input_data.csv', rows:int=100):
    with (
        open(file_name, 'w', newline='', encoding='utf-8') as f_csv,
        ):
        csv_write = csv.writer(f_csv, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        for _ in range(rows):
            new_line = []           
            new_line.append(rnd(1, 100))
            new_line.append(rnd(0, 100))
            new_line.append(rnd(0, 100))
            csv_write.writerow(new_line)        
    return

def save_to_json(func):
    def wrapper(csv_file_name:str='input_data.csv', json_file_name:str='res.json'):
        with (
            open(csv_file_name, 'r+', newline='', encoding='utf-8') as f_csv,
            open(json_file_name, 'w') as json_file
            ):
            csv_read = csv.reader(f_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            res_dic = {}
            for i, line in enumerate(csv_read):     
                # a = int(line[0])
                # b = int(line[1])
                # c = int(line[2])
                a, b, c = map(int, line)                             
                result = func(a, b, c)                
                res_dic[i] = [line, result]
            json.dump(res_dic, json_file, indent=2)
        return

    return wrapper

@save_to_json
def find_roots(a:int|float=1, b:int|float=-4, c:int|float=4):
    d = b**2 - 4*a*c
    if d >0:
        x1 = (-b - d**0.5)/(2*a)
        x2 = (-b + d**0.5)/(2*a)
        return x1, x2
    elif d == 0:
        x = -b/(2*a)
        return x
    else:
        return None


if __name__ == '__main__':
    generate_csv_file('input_data.csv', 5)    
    find_roots('input_data.csv', 'results.json')

