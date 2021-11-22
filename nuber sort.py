number = 100
number_list = []
a = 'asddfhhjk'
print(number%2, number//10)
print(a[::2])
for ch1, ch2 in zip(a[::2],a[1::2]+"_"):
    print(ch1,ch2)

while number//10 !=0:
    number_list.append(number%10)
    number = number//10
else: number_list.append(number%10)
#print(number.sort(reverse=True))
print(number%2, number//10)
number_list.sort(reverse=True)
print(number_list[0])
def max_digit (number: int) -> int:
    max_digit = lambda number: int(max(str(number)))
    return lambda number: int(max(str(number)))
n = max_digit(595595)
print(n)
# def max_digit(number: int) -> int:
#     for i in range(10)[::-1]:# взята последовательность от большего к меньшему
#         if str(i) in str(number):# есть ли и в строке от числа, если есть вернуть ( отбольшего идет)
#             return i
#    return 0

def max_digit(number: int) -> int:
    return max(map(int, str(number)))
