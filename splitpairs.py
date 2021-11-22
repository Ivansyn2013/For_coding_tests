split_pairs = 'aasbb'
split_list = []
for i in range(0,len(split_pairs),2):
    if len(split_pairs)%2 != 0:
        split_pairs = split_pairs + '_'
    split_list.append(split_pairs[i] + split_pairs[i + 1])

print( split_list)

# if len(split_pairs)%2:
#         map(split_list.append(,split_pairs)
#     return None

# лучшие решения
return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

split_pairs = lambda a: [i + k for i, k in zip(a[::2], a[1::2] + '_')]


def split_pairs(a):
    a += '_' if len(a) % 2 else ''
    return [a[i:i + 2] for i in range(0, len(a), 2)]


