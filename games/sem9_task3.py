# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from pathlib import Path

def my_json(func):
    file = Path(func.__name__+'.json')
    if file.is_file():
        with open(func.__name__+'.json', 'r', encoding='utf=8') as f:
            b = json.load(f)
    else: 
        b = {}
    def wrapper(*args, **kwargs):       
        res = kwargs    
        res['arg'] = args
        res['result'] = func(*args, **kwargs)        
        b.update(res)
        with open(func.__name__+'.json', 'w', encoding='utf=8') as f:
            json.dump(res,f)
        return res
    return wrapper

@my_json
def my_func(num = 1, *args, **kwargs):
    return num * 2

print(my_func(11, 34, num1 = 65))