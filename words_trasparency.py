'''А может быть это шифр? Может быть, но это не точно.

Вам надо проверить, что данная Строка А изометричка к Строке Б.
 Это значит что символ из Строки А может стать в соответствие символам из Строки Б.

Один символ Строки А может соответствовать только одному символу
Строки Б. Два или более символа Строки Б могут соответствовать одному символу Строки А.'''


str1= 'paper'
str2 = 'words'
z_t = [*zip(str1,str2)]

i=0
k=0
print(z_t)
for el1 in  z_t:
    for el2 in z_t[1:]:
        if el1[0] == el2[0] and el1[1] != el2[1]:
            k+=1
        if el1[0] != el2[0] and el1[1] == el2[1]:
            i+=1
print(i)
print(k)
print(True if i <= 2 and k <=1 else False)



'''
лучшие решения

isometric_strings = lambda a, b: a.translate(str.maketrans(a, b)) == b


def isometric_strings(str1: str, str2: str) -> bool:
    return len(set(zip(str1, str2))) == len(set(str1))


from pandas import DataFrame

def isometric_strings(str1: str, str2: str) -> bool:
    df = DataFrame({'str1': [x for x in str1],'str2': [x for x in str2]}).drop_duplicates()
    return not df['str1'].duplicated().any() and not df['str2'].duplicated().any()
'''