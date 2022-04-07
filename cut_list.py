import math
def split_list(items: list) -> list:
    l1 = [items[i] for i in range(0, math.ceil(len(items)/2))]
    l2 = [items[i] for i in range(math.ceil(len(items)/2), len(items))]
    print(len(items))
    print(round(len(items)/2))
    return l1, l2


print (split_list([1, 2, 3, 4, 5, 6,7,8,9]))




#лучшее решение
def split_list(items: list) -> list:
    return [items[:(split_index := (len(items) + 1) // 2)], items[split_index:]]


def split_list(items: list) -> list:
    half = -len(items) // 2
    return items[:-half], items[-half:]


def split_list(items: list) -> list:
    s = (len(items)+1) // 2
    return [items[:s],items[s:]]


# def is_acceptable_password(password: str) -> str:
#     return True if len(password) > 6 and not
#     pass.isalpha() else False

def is_acceptable_password(password: str):
    i = list(filter(str.isdigit, password))
    print((6 >= len(password)))
    print(len(i))
    return True if (6 >= len(password) and len(i) != 0) or len(password) > 9 else False

print(is_acceptable_password("short54"))