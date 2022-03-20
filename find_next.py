# def second_index(text: str, symbol: str) -> [int, None]:
#     print(text.count(symbol))
#     if text.count(symbol) == 0 or text.count(symbol) ==1:
#         return None
#     else:
#         return text.find(symbol,(text.find(symbol)+1))
#
# def frequency_sort(items):
#     counts = {x:items.count(x) for x in items}
#     sort_dict = {k:counts[k] for k in sorted(counts.keys(), key=counts.get, reverse=True)}
#     result = [x for x in sort_dict for _ in range(sort_dict[x])]
#
#     return result
#
# def frequency_sort(items):
#     return sorted(items, key=lambda x: (-items.count(x), items.index(x)))



#frequency_sort = lambda a: sorted(a, key=lambda x: (-a.count(x), a.index(x)))


def frequency_sort(items):
    i = sorted(items, key = lambda x: (items.count(x), items.index(x)) )
    return i
print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
print((frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])))
print(frequency_sort([17, 99, 42])) == [17, 99, 42]
print(frequency_sort([])) == []
print(frequency_sort([4,6,2,2,2,6,4,4,4]))

