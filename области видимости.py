# LEGB - Local Enclose Globas Built-in

# x = 'global'
# print(x)

# def some_func():
#     x = 'Enclosed item'
#     print(x)
#     def some_func2():
#         x = 'local' #последняя вложенная функция будет локальной, остальные вложенные Enclosed
#         print(x)
#     return some_func2()
# some_func()
# Можно получать данные снизу вверх, а сверху вних нельзя

# locals() globals()
# print(globals())
# x = 'Some data'
# def func():
#     pass
# print(x is globals()['x'])
# globals()['new key'] = 'Hello world'

# print(locals())
# def some_func():
#     some_string = 'hello'
#     locals()['num'] = 525
#     print(locals())

#     def func():
#             print(locals())
# some_func()

# def func():
#     print(globals())
# func()


# global nonlocal
# x = 0
# def counter():
#     global x
#     print(x)
#     x+=1
# print(counter())
# print(counter())
# print(counter())
# print(counter())

# counter()
# counter()
# counter()
# print(f'Это 3начение глобальной переменной 3')

# nonlocal
# x = 100
# def f():
#     x = 20
#     def g():
#         nonlocal x
#         x = 40
#     g()
#     print(x)
# f()


# def some_func():
#     x = 100
#     z = 'hello'
#     return 
#     print(f'{x} {z}')
# после return написанное внутри функции не работает, в данном случае print
# return выдает результат и заканчивает работу функции
# some_func()








