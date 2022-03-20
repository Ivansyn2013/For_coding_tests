# Nearest ValueNearest Value
#  Elementary+
# EN PL JA Russian
# Найдите ближайшее значение к переданному.
#
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
#
# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.
#
# Несколько уточнений:
#
# Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# Ряд чисел всегда не пустой, т.е. размер >= 1;
# Переданное значение может быть в этом ряде, а значит оно и является ответом;
# В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# Ряд не отсортирован и состоит из уникальных чисел.
# Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
#


def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    else:
        set_list = list(values)
        set_list.append(one)
        set_list.sort()

        i = set_list.index(one)
        if set_list[i] == set_list[-1]:
            return set_list[-2]
        if set_list[i] == set_list[0]:
            return set_list[1]
        if set_list[i] - set_list[i - 1] == set_list[i + 1] - set_list[i]:
            return set_list[i - 1]

        elif set_list[i] - set_list[i - 1] > set_list[i + 1] - set_list[i]:
            return set_list[i + 1]
        elif set_list[i] - set_list[i - 1] < set_list[i + 1] - set_list[i]:
            return set_list[i - 1]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")



# лучшие решениея
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")


from functools import cmp_to_key
def nearest_value(values: set, one: int) -> int:
    return sorted(values, key = cmp_to_key(lambda a,b: abs(a - one) - abs(b - one) or (a-b)))[0]
