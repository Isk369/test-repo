# {key:value, key:value}
# dct = {}
# print(type(dct))

# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# print(dct['hobby'][1])

# Методы словарей
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# dct.clear()
# print(dct)

# dict.copy() -копирование словаря
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# dct1 = dct.copy()
# print(dct1)


# dict.fromkeys(seq[, value]) создает словарь 
# с ключами из q значениями value по умолчанию None
# lst = ['name', 'age', 'hobby']
# dct =dict.fromkeys(lst, 1000)
# print(dct)


# dict.get(key[, default]) в отличии от обычного 
# принта не выдает ошибку если такого нет а пишет None
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# print(dct.get('surname'))

# dict.items() возвращает список кортежей ключ-значение
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# lst = list(dct.items())
# print(lst[0])


# dict.keys() -возвращает список из ключей
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# print(dct.keys())

# dict.values() -возвращает список из значений
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# print(dct.values())

# dict.pop(key[, default]) - удаляет элемент по ключу, если нет default то ошибка
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# remove_element = dct.pop('surname', 'Нет такого ключа')
# print(f'Это удаленный элемент {remove_element}\n это сам словарь {dct}')

# dict.popitem() - удаляет рандомную пару ключ-значение
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# remove_element = dct.popitem()
# print(remove_element)

# dict.setdefault(key[, default]) возвращает значение по ключу, если такого нет, 
# то создаст со значением None по умолчанию
# dct = {'name': 'John','age': 25, 'hobby': ['fishing', 'football', 'auto']}
# elem = dct.setdefault('surname', 'Jackson')
# print(f'Это значение {elem}, а это сам словарь{dct}')

# dict.update([other]) - доюавляет элемент
# dct = {'name': 'John','age': 25}
# dct.update({'surname': 'Jackson', 'hobby': 'fishing'})
# print(dct)

# Циклы в словарях
# dct = {'name': 'John', 'age': 25, 'surname': 'Jackson', 'hobby': 'fishing'}
# for k, v in dct.items():
#     print(f'Это ключ {k}, это значение {v}')
# for k in dct.items():
#     print(k)

# tuple - кортеж
# tpl = tuple()
# tpl1 = ()
# print(type(tpl))

# tpl = ('Hello', [1, 2])
# tpl[1].append('3')
# print(tpl[1][2])

# for i in tpl:
#     print(i)

# print(tpl[0].upper())

# index(), count()
# tpl = ('hello', 'world', 11, 22)
# print(tpl.count('hello'))
# print(tpl.index(11))

# frozenset отличие от множества то что  fstнеизменяемый
# st = {'hello', 1, 2, 'world'}
# fst = frozenset(st.copy())
# print(type(fst))