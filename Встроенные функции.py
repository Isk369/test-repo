# def add_nums(a, b):
#     return a+b
# result = add_nums(10, 5)
# print(result)


# result = lambda a, b: a + b  работает по типу функции, после двоеточия идет авто return
# print(result(10, 8))
# print(type(result))

# map() 

# lst = [1, 2, 3, 4, 5]
# lst_new = [str(i) for i in lst]
# for i in lst:
#     lst_new.append(str(i))
# print(lst_new)
# map(function, iterible_obj)
# def num_to_str(i):
#     return str(i)
# lst_new = list(map(lambda i: str(i), lst))
# lst_new = list(map(num_to_str, lst))
# print(lst_new)

# filter()
# filter(function, iterible_obj)
# lst = [i for i in range(1, 11)]
# lst = list(range(1, 11))
# print(lst)
# new_lst = list(filter(lambda x: x%3 != 0, lst))
# print(new_lst)

# reduce()
# from functools import reduce
# lst = [20, 2, 3, 5]
# result = reduce(lambda x, y: x - y, lst)
# print(result)

# pow()
# print(pow(3, 2)) возводит в степень

# zip() Архивирует данные, совмещает. Кол-во аргументов должно совпадать
# employe_number = [2, 9, 28 ,18, 50]
# employe_names = ['John', 'Sam', 'Tom', 'James']
# employe_sphere = ['IT', 'Broker', 'Cook', 'Banker']
# zipped_values = zip(employe_number, employe_names, employe_sphere)
# # print(zipped_values)
# zipped_list = list(zipped_values)
# print(zipped_list)


# try:
#     if 
#     print(10/0)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')
# raise ValueError

# else:

# Finally:
# def sum_digits(a):
#     d1 = a%10
#     x = a//10
#     d2 = x % 10
#     y = x//10
#     return d1 + d2
# print(sum_digits(150))

a = 150
b = list(a)
# def sum_digits(a):
#     b = list(a).split()
#     sum_ = sum(b)
#     return sum_
# print(sum_digits(150))
print(b)