'''Дан непустой массив целых чисел (X). В этой задаче вам нужно вернуть массив,
состоящий только из неуникальных элементов данного массива. Для этого необходимо удалить
 все уникальные элементы (которые присутствуют в данном массиве только один раз).
 Для решения этой задачи не меняйте оригинальный порядок элементов.
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].'''


digitals = [1,2,3,4,4,4,4]
w = []
print(digitals.count(2))
for x in digitals:
    if digitals.count(x) > 1:
        w.append(x)
    else:continue
print(w)
def checkio(data):
    return [x for x in data if data.count(x)>1]