# 1.# lst = [i if i % 3 == 0 and i % 5 == 0 else 'неизвестно' for i in range(1, 101)]
# # print(lst)


# 2. dct = {'hello': None, 'World': None, 'programmer': None}
# dct = {k: len(k) for k, v in dct.items()}
# print(dct)



# users = {'Alex': 'hello'}
# def login(name):
#     print(f'User, {name}. Youre are login succesfully!')


# C-create, R-read/retrive, U-update, D-delete
# from typing import AsyncGenerator


db = {'John':23, 'Jack':52, 'Alex':23, 'Tom': 34}
# def  create():
#     global db
#     name = input('Enter name: ')
#     age = int(input('Enter age: '))
#     if name in db:
#         print('Пользователь уже существует!')
#     else:
#         db['name'] = age
#         print('Пользователь добавлен')
#         print(f'На данный момент список пользователей такой: {db}')
# create()
# def read():
#     print(f'На данный момент содержание такое: {db}')
# read()
# def update():
#     global db
#     name = (input('Кого вы хотите изменить: '))
#     age - int(input('Enter new age: '))
#     if name in db:
#         db[name] = age 
#         print(f'Пользователь успешно изменен!')
#         print(f'Саисок на данный момент такой: {db}')

def delete():
    name = input('Enter name you want to delete: ')
    if name in db:
        db.pop(name)
        print('User is removed', db)
    else:
        print('Error')
delete()







# def read():
#     pass
# def update():
#     pass
# def delete():
#     pass





