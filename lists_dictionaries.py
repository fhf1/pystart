#                            LISTS

phones = ["iPhone Xs", "Xiaomi Mi8", "Samsung 10s", "iPhone 9", "iPhone 9"]

print(phones)

phones_count = len(phones)
print(phones_count)

# Добавление в конец списка
phones.append("iPhone 6")
print(phones)

print(phones.count("iPhone 6"))
print(phones.count("iPhone 9"))

print(phones[0])
# print(phones[4])

# Срезы из списка (взять все элементы, начиная с 1, заканчивая 3, но не включая сам третий)
print(phones[1:3])
# взять первый элемент с конца
print(phones[-1])
# Если начальной границы среза нет, то взять с нулевого элемента
print(phones[:2])
# Поиск по индексу номер порядкового элемента списка
print(phones.index("iPhone 6"))
print(phones[3])
# Сортировка (идет сначала по заглавным буквам, затем - по строчным). Если в списке есть разные типы данных, то сортировка не сработает.
phones.sort()
print(phones)
# Проверка на вхождение элемента в списке
print("iPhone 6" in phones)
# Удаление элемента по индексу
print(phones)
print(f'Четвертый элемент отсортированного списка: {phones[4]}')
del phones[4]
print(phones)
print(f'Четвертый элемент отсортированного списка: {phones[4]}')
# Удаление элемента по названию (первого встречающегося элемента с таким названием)
phones.remove("iPhone Xs")
print(phones)

#                            DICTIONARIES

product = {
    "name": "iPhone Xs",
    "stock": 5,
    "price": 65000.0
    }
# Если ключ есть, а мы присваиваем, то значение ключа обновляется:
product["stock"] = 10
print(product)
print(len(product))
# Если ключа нет, он будет создан:
product["memory"] = 64
print(product)
# Получаем значение элемента по его ключу:
print(product['name'])
# Безопасное обращение по ключу:
# по существующему ключу:
print(product.get('name'))
# по отсутствующему ключу (вернется None):
print(product.get('discount'))
# .get позволяет вернуть значение по умолчанию (когда такого ключа нет):
print(product.get('discount', 0))
# Удаление элемента
print(product)
del product['stock']
print(product)

# Списки и словари можно объединять

# Наш список для словаря и его ключа 'recommend'
product['recommend'] = phones
print(product)
# Получение элемента из вложенного в словарь списка:
print(product['recommend'][1])
# Добавление элемента в список, вложенный в словарь:
product['recommend'].append("iPhone 7")
print(product)

print('\nСПИСОК СЛОВАРЕЙ (часто используется в разработке, например, как список товаров):\n')
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5},
]

print(stock)
print(f'Первый словарь из списка словарей:\n{stock[0]}')
print(f'Значение первого ключа из первого словаря списка словарей:\n{stock[0]["name"]}')

print('\nМеняем цену:\n')
print(stock[0])
stock[0]['price'] += 10000
print(stock[0])

print(type(stock))
print(type(stock[0]['recomended']))
print(type(stock[0]['recomended'][1]))
print(stock[0]['recomended'][1])
