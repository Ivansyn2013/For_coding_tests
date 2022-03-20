bigger_price = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]

rr = sorted([el.get('price') for el in bigger_price], reverse=True)
print(rr)
result = (el for el in bigger_price if el.get('price') == max(el.get('price') for el in bigger_price))


rr = sorted(bigger_price, key=lambda x: x.get('price'), reverse=True)



print(*result)