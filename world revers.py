line = 'world'

l1 = []
result = ''


for x in line:
    if x.isalpha():
        l1.append(x)

    else:
        l1 = l1[::-1]
        result = result + ''.join(l1) + x
        l1 = []
else:
    l1 = l1[::-1]
    result = result + ''.join(l1)





print (result)


print(line)



def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))
