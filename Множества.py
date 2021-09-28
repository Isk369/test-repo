# a = {'hello', 1, 2}
# print(a)
# for i in a:
#     print(i)

# lst = ['456', '325', '456', '856', '789', '325']
# a = set(lst)
# lst = list(a)
# print(lst)
# set{} оставляет только уникальные объекты, удаляет повторные

# a = []
# пустой список
# пустое множество set()

# Операции над множеством
# a = {'hello', 1, 2}
# print(len(a))

# a = {'hello', 1, 2}
# print('hello' in a)

# set.isdisjoint(other)
# a = {'hello', 1, 2}
# b = {'world', 5, 'John'}
# print(a.isdisjoint(b))
# isdisjoint показывает True если переменные не имеют ничего общего

# set == other
# a = {'hello', 1, 2}
# b = {'world', 5, 'John'}
# c = {'world', 5, 'John'}
# print(c == b)
# В set '==' Показывает True если элементы совпадают

# set/issubset(other)
# a = {'world', 5, 'John', 'Tom'}
# b = {'world', 5, 'John'}
# print(b.issubset(a))
# issubset - подмножество, если есть элементы из 'a' то дает True, если 'b' является его подмножеством
# print(b <= a) тоже самое что и issubset

# set.issuperset(other) Надмножество
# a = {'world', 5, 'John', 'Tom'}
# b = {'world', 5, 'John'}
# # print(a.issuperset(b))
# print(a >= b) то же самое

# set.union(other, ...) Объединяет множества
# a = {'world', 5, 'John', 'Tom'}
# b = {'world', 5, 'John'}
# c = {15, 'Jack'}
# # print(b.union(c, a))
# print (a | b | c) тоже самое

# set.intersection(other, ...) пересечение множеств
# a = {'world', 5, 'John', 'Tom'}
# b = {'world', 5, 'John'}
# c = {15, 'Jack'}
# print(b.intersection(a))
# print(b & a) тоже самое
# Показывает одинаковые переменные внутри множества

# set.difference(other, ...) разница
# a = {'world', 5, 'John', 'Tom'}
# b = {'world', 5, 'John'}
# c = {15, 'Jack'}
# # print(b.difference(c)) показывает что есть в b чего нет в c
# print(b - c) тоже самое

# set.symmetric_difference(other, ...) 
# a = {'world', 5, 'John', 'Tom'}
# b = { 5, 7, 'John'}
# c = {15, 'Jack', 'Tom'}
# print(b.symmetric_difference(c)) показывает уникальные переменные в обеих переменных 
#  print(b ^ c) тоже самое

# set.copy() копирование множества
# a = {'world', 5, 'John', 'Tom'}
# b =a.copy()
# print(b)

# Операции изменяющие множества

# set.update(other, ...)
# a = {'world', 5, 'John', 'Tom'}
# b = { 5, 7, 'John'}
# a.update(b)
# print(a) добавляет элементы из другого множества
# print(b |= c) тоже самое


# set.intersection_update(other, ...) обновление пересечением
# a = {'world', 5, 'John', 'Tom'}
# b = { 5, 7, 'Hello'}
# a.intersection_update(b)
# print(a)
# print(a) добавляет элементы из другого множества
# print(b &= c) тоже самое


# set.difference_update(other, ...) обновление разницой
# a = {'world', 5, 'John', 'Tom'}
# b = { 5, 7, 'Hello'}
# a.difference_update(b)
# print(a)
# print(a) добавляет элементы из другого множества
# print(a -= b) тоже самое

# # set.symmetric_difference_update(other, ...) обновление разницой в обе стороны
# a = {'world', 5, 'John', 'Tom'}
# b = { 5, 7, 'Hello'}
# a.symmetric_difference_update(b)
# print(a)
# print(a) добавляет элементы из другого множества
# print(a ^= b) тоже самое

# # set.add(elem) добавление элемента в множество
# b = { 5, 7, 'Hello'}
# b.add('hello')
# print(b)


# set.remove(elem) удаляет если есть элемент, если нету то выбрасывает ошибку key error
# b = { 5, 7, 'Hello'}
# b.remove(5)
# print(b)

# set.discard(elem) удаляет если есть таакой элемент, если нет то ничего не делает(не выдает ошибку)
# b = { 5, 7, 'Hello'}
# b.discard(5) принимает только один аргумент
# print(b)

# set.pop() удаляет элемент выборочно, так как множество неупорядоченно, удаляет как рулетка
# b = { 5, 7, 'Hello'}
# b.pop()
# print(b)

# set.clear() очистка множества
# b = { 5, 7, 'Hello'}
# b.clear()
# print(b)



















