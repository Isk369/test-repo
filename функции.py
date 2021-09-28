# def add_func():
#     print(10+5)
# add_func()

# def add_nums():
#     pass-потом можно дописать функцию
# def add_nums(first, second):
#     print(first+second)
# num1 = int(input('first num'))
# num2 = int(input('second num'))
# add_nums(num1, num2)

# def add_nums(num1, num2):
#     return num1+num2  возвращает в принте result результат
# result = add_nums(10, 100)   #110 
# print(result)

# def hello(name, surname, age):
#     print(f'Привет {name} {surname}!' f'Тебе уже {age} лет! Это круто!')
# name, surname, age = input('Enter your name'), input('Enter your surname'), int(input('Enter your age'))

# hello(name, surname, age)   
# hello('Alex', 'N', 23) # Тоже самое
# hello(age = 23, name = 'Alex', suename = 'N') # Тоже самое, можно менять местами переменные


# def hello(age, name = 'Неизвестно', surname = 'Неизвестно'): #Дефолтные значения
#     print(f'Привет {name} {surname}!' f'Тебе уже {age} лет! Это круто!')

# hello(age = 23)

# def func(*args, **kwargs):
#     print(f'Это арги {args}')
#     print(f'Это кварги {kwargs}')
# func('hello', 'j', 1, 52, name = 'Alex', surname = 'N', age = 23)
# внутри аргс хранится tuple
# внутри кваргс хранится словарь dict

# ЧЕТКИЙ КАЛЬКУЛЯТОР(num1, num2):
# def add_func(num1, num2):
#     return num1+num2

# def sub_func(num1, num2):
#     return num1-num2

# def mult_func(num1, num2):
#     return num1*num2

# def div_func(num1, num2):
#     return num1/num2

# def handler(operation, num1, num2):
#     switcher = {
#         '+': add_func(num1, num2),
#         '-': sub_func(num1, num2),
#         '*': mult_func(num1, num2),
#         '/': div_func(num1, num2)
#     }
#     return switcher[operation]

# num1 = int(input('Enter first num: '))
# operation = input('Chosse from "+", "-", "*", "/"')
# num2 = int(input('Enter second num: '))

# result = handler(operation, num1, num2)
# print(result)


# Перевод языка клавиатуры англ рус если вдруг ошибся с раскладкой
# string = input('Введите строку: ').lower()

# def translate_str(string):
#     intab = "qwertyuiop[]asdfghjkl;'\zxcvbnm,./"
#     outtab = "йцукенгшщзхъфывапролджэ\ячсмитьбю."
#     trantab = str.maketrans(intab, outtab)
#     return string.translate(trantab)

# result = translate_str(string)
# print(result)








