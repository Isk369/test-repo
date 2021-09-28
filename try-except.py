# Try-except 

# try:
#     a = 'Azamat'
#     (logic expression)
# except NameError:
#     print(a)

# try:
#     num1 = 1
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print('На ноль делить модно')

# SyntaxError TabError IndentationError Исключения

# try:
#     a = int(input("Введите число: "))
#     b = int(input("Введите что-нибудь: "))
#     print(a / b)
# except TypeError, ZeroDivisionError, OSError:
#     print("OK")

# try:
#     num1 = int(input("Enter first num: "))
#     num2 = int(input("Enter second num: "))
#     num1/num2

# except:
#     print('You can not divide by zero!')
#     raise Показывает автоматом тип ошибки
# else:
#     print('Successfully divided!')
# finally:
#     print("Worked!!!")

# try:
#     num1 = int(input('Введите первое число: '))
#     operations = input("Выберите один оператор: '+', '-', '*', '/'")
#     num2 = int(input ("Введите второе число: "))
#     operations_dict = {'-':num1 - num2, '+': num1 + num2, '*': num1*num2, '/': num1/num2} 
#     print(operations_dict[operations])
# except ArithmeticError:
#     print('Вводите только числа!ArithmeticError!')
# else: 
#     print('Вычисление выполнено!')
# finally: 
#     print('Krasava')

x = 10  
y = 5
print(x%y)



