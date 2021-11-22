items = []
l = items
print(items[0::-1])
for x in items[0::-1]:
    items.append(x)
print(items[1:] if items != [] else items)
# лучшие решения
print(list(lambda l: l[1%len(l):]+l[:1%len(l)] if not len(l)==0 else l))


if items:# не понимаю что дает наверное None
        items.append(items.pop(0))
print()