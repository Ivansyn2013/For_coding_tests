
def is_all_upper(text: str) -> bool:
    res = list(filter(str.isupper, text.split(' ')))
    return True if len(res) == len( text.split(' ')) else False


#print(is_all_upper('S a'))

x=0
y=0

for x, y in ((0,0),(1,0),(0,1),(1,1)):
    print(x , y, end=' ')
    print(x & y,end=' ')
    print(x | y, end=' ')
    print(x ^ y, end=' ')
    print (x ** y,end=' ')
    print((x and y) ** (x or y),end=' ')
    print((x * y))



# что   это????
boolean=lambda x,y,o:1&~"dimpleqonx".index(o[1])>>y>>x>>y


def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0



OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

boolean=lambda x,y,o:{'co':x and y,'di':x or y,'im':y if x else 1,'ex':x!=y,'eq':x==y}[o[:2]]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
