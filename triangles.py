import math
from itertools import product

def side_s(a):
    ab = [*map(lambda x,y:y-x,a[0],a[1])]
    bc = [*map(lambda x,y:y-x,a[1],a[2])]
    ca = [*map(lambda x,y:y-x,a[2],a[0])]
    ab = (pow(ab[0],2)+pow(ab[1],2))
    bc = (pow(bc[0],2) + pow(bc[1],2))
    ca = (pow(ca[0], 2) + pow(ca[1],2))
    return [ab,bc,ca]
def pod_trig(coords_1, coords_2):


    res = [*map(lambda x, y: x / y, sorted(side_s(coords_1)), sorted((side_s(coords_2))))]
    print(res)
    return True if len(set(res)) == 1 else False


print(pod_trig([[-4,-1],[-3,2],[-4,2]],[[10,1],[-8,1],[-8,7]]))


#подобие треугольников лучшие решения
from itertools import starmap
from sympy.geometry import Point, Polygon, are_similar

def poly(points):
    return Polygon(*starmap(Point, points))

def similar_triangles(coords_1, coords_2):
    return are_similar(poly(coords_1), poly(coords_2))




i=__import__
s=lambda T:sorted((z-x)**2+(t-y)**2for(x,y),(z,t)in i('itertools').combinations(T,2))
similar_triangles=lambda*T:len(set(map(i('fractions').Fraction,*map(s,T))))==1





from typing import List, Tuple
Coords = List[Tuple[int, int]]

def similar_triangles(c1, c2) -> bool:
# The list of two arrays of the squares of the lengths of the sides of the triangles:
  s = [[(c[k-1][0] - c[k][0]) ** 2 + (c[k-1][1] - c[k][1]) ** 2 for k in range(3)] for c in (c1, c2)]
# If the triangles are similar, then the ratio of the corresponding sides are equal:
  return len(set(sorted(s[0])[i] / sorted(s[1])[i] for i in range(3))) == 1