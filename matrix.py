def checkio1(matrix: list[list[int]]) -> bool:
    l=matrix
    k=[]
    for x in range(len(l)):
        for y in range(len(l[x])):
            k = [str(x) for x in l[x]]
            if ''.join(k).find(str(l[x][y])*4) != -1:
                return  True
            if x < (len(l)-3):
                if l[x][y] == l[x+1][y]== l[x+2][y] == l[x+3][y]:

                    return True

            if 3 <= y and x < (len(l)-3):
                print('index', x, y, 'z', l[x][y])
                if l[x][y] == l[x+1][y-1] == l[x+2][y-2] == l[x+3][y-3]:

                    return True
            if  y < (len(l[0])-3) and x < (len(l)-3):
                #print('index',x,y,'z',l[x][y])
                if l[x][y] == l[x+1][y+1] == l[x+2][y+2] == l[x+3][y+3]:

                    return True
    return False






DIR = [(dx, dy) for dy in range(-1, 2)
                    for dx in range(-1, 2)
                    if dx != 0 or dy != 0]

print(DIR)




def checkio2(matrix):
    N = len(matrix)
    def seq_len(x, y, dx, dy, num):
        # функция берет кординаты и дельты координат заданные через констанету DIR
        # пото сравнивае число по кординатам с переданным в аргументах возвращает число попаданий
        if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
            return 1 + seq_len(x + dx, y + dy, dx, dy, num)
        else:
            return 0

    DIR = [(dx, dy) for dy in range(-1, 2)
                    for dx in range(-1, 2)
                    if dx != 0 or dy != 0]
    for y in range(N):
        for x in range(N):
            for dx, dy in DIR:
                if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
                    return True
    return False

def checkio3(data):
    '''функция возвращает знгачение по координатам, если они не проходят проверку, то нан
        значение передается в сет, где проверяется его диллая , все это завернуто any даещий true если в
        последовательности хотя бы один True.
        математи ходов (0,1),(1,1),(1,0),(1,-1) это ходы по вертикали и горизонтале, и двум диагоналям
        к коэффициент повторений'''


    def g(i, j):
        if 0 <= i < n and 0 <= j < n: return data[i][j]

    return any(len({g(p//n+d*k,p%n+e*k) for k in range(4)}) == 1 for p in range(n * n) for d, e in [(0, 1), (1, 1), (1, 0), (1, -1)])



