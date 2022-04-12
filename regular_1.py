def checkio(data):
    stack=[""]
    brackets={"(":")","[":"]","{":"}"}
    for c in data:
        if c in brackets:
            stack.append(brackets[c])
        elif c in brackets.values() and c!=stack.pop():
            return False
    return stack==[""]


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"


print(checkio('(3+{1-1)}'))



import re
checkio=c=lambda e,d=500:d and c(re.sub(r'[^][(){}]|\(\)|\{}|\[]','',e),d-1)or not e


def checkio(expression):
    s = ''.join([c for c in expression if c in '{}()[]'])
    old = 0
    while old != len(s):
        old = len(s)
        s = s.replace('{}', '').replace('()', '').replace('[]', '')
    return len(s) == 0

    # Remove '{}', '()', '[]' until can't remove.


brackets = (('(', ')'), ('{', '}'), ('[', ']'))

def checkio(expression):
    last = []
    for i in expression:
        if i in '({[':
            last += [i]
        if i in ')}]':
            if not last or (last.pop(), i) not in brackets:
                return False
    return not last



def checkio(eq):
    res = [0]   #to avoid pop() from empty list in case of ")1+3"
    for c in eq:
        if c in ("(","[","{"):
            res.append(c)
        elif c == ")" and "("!= res.pop():
            return False
        elif c == "]" and "["!= res.pop():
            return False
        elif c == "}" and "{"!= res.pop():
            return False
    res.pop(0)
    return not res