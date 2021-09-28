# fruits = ['apple', 'banana', 'grapes']
# for i in fruits:
#     if i == 'banana':
#         continue
#     print(i)

# a = 4
# b = 5
# a = b  Присвоение
# print(a)

# a = 4
# b = 5
# a,b = b,a  Присвоение в обе стороны
# print(a)
# print(b)

# print(a := 2 + 4) Моржовый оператор позволяет сразу прибавлять во время принта ':='

# while value := input(("Enter something:")!= ""):
#     print('Nice')

# Задача
# lst = ['a', 'sbbb', 'asdsdfsdfsdfsdff', 'sdfghfghf']
# lst = ['shorter'  if len(i)<= 4 else 'longer' for i in lst]
# print(lst)
# Если переменная меньше 4 символов писать Shorter
# если иначе то longer

# a = {'a':1, 'b':5, 'c':4, 'd':3}
# dict_ = {k: list(range(1, v+1)) for k, v in a.items()}
# print(dict_)
# k = ключ
# v = значение

# a = int(input("Сколько у Вас в бумажнике?: "))
# if a<0:
#     raise ValueError("Сумма не может быть отрицательной!")
# else:
#     print(a)

# Найти максимальное значение 
# dict_ = {'Timur':{'h':90, 'm':95, 'l':91}, 'Vlad': {'m':93, 'v':95, 'l':98}}
# dict_ = {k1:k2 for k1, v1 in dict_.items() 
# for k2, v2 in v1.items() 
# if max(v1.values()) == v2}
# print(dict_)

# dict_ = {'first': {'a': 1}, 'second': {'b':2}}
# dict_ = {k1:v2 for k1, v1 in dict_.items() for v2 in v1.items()}
# print(dict_)

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#     # if not age in range (1,85):
#         raise ValueError("Forbidden")
# except ValueError:
#     print("Your age must be 18+")
# else:
#     print("OK")
# finally:
#     print("Good Bye")

# Задача написать код для того чтобы компзагадывал рандомное число и выдавал ответ пользователю
# import random
# a = (random.randrange(0,10))
# while True:
#     num = input("Введите число: ")
#     print(f"Число загаданное компьютером: {a}")

#     if num.lower() == "exit":
#         print("Game Over")
#     elif int(a)>int(num):
#         print("Число больше")
#     elif int(a)<int(num):
#         print("Число меньше")
#     elif int(a)==int(num):
#         print("Поздравляю, Вы угадали!")
#         print("Напишите exit для выхода")


