number = '100001010'
i=0
m = 2
i=10 if map(lambda i: i == '0', number)
print(list(map(lambda i: i == '0', number)))
print(i)


# лучшее решение
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))