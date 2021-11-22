i = '   '

# print(i.isupper())
# print(i.isdigit())
# print(i.isalpha())
n = list(map(lambda x: x.islower() == True, i))
b = True
for i in n:
    if i == True:
       b = False
       break
    else: b = True
print(*n)
print(b)


# best solution

    text = text + "A"
    return text.isupper()

return text.upper() == text