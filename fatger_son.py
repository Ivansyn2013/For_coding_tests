def is_family(tree: list[list[str]]) -> bool:
    if len(tree) < 2:
        return True
    first_p = []
    second_p = []
    for el in tree:
        if el[::-1] in tree:
            return False
        first_p.append(el[0])
        second_p.append(el[1])

    for el in tree:
        f = first_p.copy()
        f.remove(el[0])
        s = second_p.copy()
        s.remove(el[1])
        if s.count(el[0]) > 1 and f.count(el[1]) > 1:
            return False
        elif el[0] in f and el[1] in s:
            return False
        elif f.count(el[0]) > 1 and el[0] not in s:
            return False
        elif el[0] not in f and el[0] not in s and el[1] not in f:
            return False

    return True




#Clear solution
from collections import defaultdict
def is_family(tree):
    anscestor = defaultdict(set)
    for father, son in tree:
        if father == son: return False
        if father in anscestor[son]: return False
        if son in anscestor[father]: return False
        if anscestor[father] & anscestor[son]: return False
        anscestor[son] |= {father} | anscestor[father]
    adam = [person for person in anscestor if not anscestor[person]]
    return len(adam) == 1


#Creative solution

from contextlib import suppress


def is_family(tree):
    with suppress(AssertionError, RecursionError):
        f = {}
        for father, son in tree:
            assert son not in f
            f[son] = father

        def oldest_ancestor(person):
            with suppress(KeyError):
                return oldest_ancestor(f[person])
            return person

        patriarchs = set(map(oldest_ancestor, f))
        return len(patriarchs) == 1

    return False


#Speed solution
from collections import defaultdict


def is_family(tree: list[list[str]]) -> bool:
    ancestors = defaultdict(set)
    for father, son in tree:
        if (   father == son or ancestors[son] or son in ancestors[father]
            or ancestors[father] & ancestors[son]
        ):
            return False
        ancestors[son] = {father} | ancestors[father]
    roots = 0
    for man in ancestors:
        if not ancestors[man]:
            roots += 1
            if roots > 1:
                return False
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'one father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'grant father'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father for your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father for your brather?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
