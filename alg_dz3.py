'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
из чисел в диапазоне от 2 до 9.
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан
массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива с
тоят четные числа.
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
4. Определить, какое число в массиве встречается чаще всего.
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
7. В одномерном массиве целых чисел определить два наименьших элемента. Они
могут быть как равны между собой (оба являться минимальными), так и различаться.
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
последнюю ячейку строки. В конце следует вывести полученную матрицу.
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random
# 1
def multiple():
    a = [x for x in range(2, 100)]
    res = {}

    for i in a:
        for ii in range(2, 10):
            if i % ii == 0:
                res.setdefault(ii, []).append(i)

    return res


# 2
def even_store(nums: list):
    if type(nums) != list or len(nums) < 2:
        return 'Ошибка значений'
    else:
        res = []
        for ind, elm in enumerate(nums):
            if elm % 2 == 0:
                res.append(ind)
        return res


#3
def change_places():
    a = []
    for x in range(10):
        a.append(random.randint(0,10))
    print(a)
    a_max = a.index(max(a))
    a_min = a.index(min(a))
    a[a_max],a[a_min] = a[a_min],a[a_max]

    return a

# 1
# print(multiple())
# 2
#print(even_store([2, 3, 6, 7, 9, 10]))
#print(even_store(2))


#3
print(change_places())