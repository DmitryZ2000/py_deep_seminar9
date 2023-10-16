# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from random import randint as rnd


def generate_csv_file(csv_file_name:str='input_data.csv', rows:int=100):
    with (
        open(csv_file_name, 'w', newline='', encoding='utf-8') as f_csv
        ):
        csv_write = csv.writer(f_csv, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        # first_line = ['num_1', 'num_2', 'num_3']
        # csv_write.writerow(first_line)
        for _ in range(rows):
            new_line = []           
            new_line.append(rnd(1, 100))
            new_line.append(rnd(0, 100))
            new_line.append(rnd(0, 100))
            csv_write.writerow(new_line)        
    return

def get_data_from_csv(func):
    def wrapper(csv_file_name:str='input_data.csv'):
        with (
            open(csv_file_name, 'r+', newline='', encoding='utf-8') as f_csv            
            ):
            csv_read = csv.reader(f_csv, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            res_dic = {}
            for i, line in enumerate(csv_read):
                a, b, c = map(int, line) 
                # print(f'Запускаю {func.__name__}')                
                result = func(a, b, c)
                res_dic[i] = [line, result]
        return res_dic

    return wrapper

def save_to_json(func):
    def wrapper(json_file_name:str='results.json'):
        with (
            open(json_file_name, 'w') as json_file
            ):
            new_dict = func() 
            json.dump(new_dict, json_file, indent=2)
        return
    return wrapper



# def save_to_json(new_dict, json_file_name:str='results.json'):
#     with (
#         open(json_file_name, 'w') as json_file
#         ):
#         json.dump(new_dict, json_file, indent=2)
#     return

@save_to_json
@get_data_from_csv
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
    generate_csv_file('input_data.csv', 50)
    find_roots()

