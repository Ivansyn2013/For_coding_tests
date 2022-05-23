import itertools
def verify_anagrams(a, b):
    i = list(a.lower().replace(' ',''))
    ii = list(b.lower().replace(' ',''))
    for w in i:
        try:
            ii.remove(w)
        except ValueError:
            return False
    return True if ii == [] else False


print(verify_anagrams('Programming', 'Gram Ring Mo'))