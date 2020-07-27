# price = 100
# discount = 20
# price_with_discount = price - price * discount / 100
# print(price_with_discount)

def discounted(price, discount, max_discount=60):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)

discounted(100, 101)
print(discounted(200, 70, max_discount=100))
# discounted(200, -30)
# discounted(-400, 10)
# p = discounted(150, 50)
# print(p)

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 50}

product['with_discount'] = discounted(product['price'], product['discount'])

print(product)