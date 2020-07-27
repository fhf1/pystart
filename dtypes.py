# a = "Привет"
# b = 'мир'
# c = 2
# c = '{}, {}{}!'.format(a, b, c)
# print(c)

# user = 'Python'
# c = 'Привет {name}!'.format(name=user)
# print(c)

# user = 'Python'
# c = f'Привет {user}!'
# print(c)

# a = 'Привет'
# b = 'мир'
# c = f'{a} {b}!'
# print(len(c))

# a = 'Привет'.upper()
# print(a)

# b = 'МИР'.lower()
# print(b)

# c = 'learn python'.capitalize()
# print(c)

# a = '   Mike    '
# b = a.strip()
# print(len(a))
# print(len(b))

# a = 'H3llo m3m3!'
# b = a.replace('3', 'e')
# print(b)

# a = 'Привет мир!'
# b = a.replace('мир', 'python')
# print(b)

# a = 'Привет приветЫ'.lower().replace('ы', '').capitalize()
# print(a)

# Разбиение строки в список
# a = "learn.python.ru"
# print(a.split('.'))

# Простой способ подсчета кол-ва слов в предложении
# a = "Предложение из нескольких слов 123"
# b = a.split()
# print(b)
# print(len(b))

# a = None
# b = 0
# print(a is None)
# print(b is not None)

# a = 2.0
# b = '2.0'
# c = 2
# d = True
# e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# Ввод от пользователя
# name = input('Введите ваше имя: ')
# print(f'Привет {name}!')

# age = input('В каком году вы родились? ')
# # input возвращает строковый тип данных
# print(type(age))
# age = 2020 - int(age)
# print(f'Ваш возраст: {age}')

# # ИЛИ так:
# age = int(input('В каком году вы родились? '))
# print(type(age))
# age = 2020 - (age)
# print(f'Ваш возраст: {age}')

# print(bool('Hello!'))
# print(bool(''))
# print(bool(1))
# print(bool(0))
# print(bool(0.1))
# print(bool(-2))
# print(bool(None))