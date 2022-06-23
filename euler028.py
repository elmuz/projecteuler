def spiral(N):

    M = [[0 for x in range(N)] for y in range(N)] 

    M[N // 2][N // 2] = 1
    x = N // 2
    y = N // 2
    n = 1
    M[x][y] = n
    #print(M)

    for c in range(1, (N // 2) + 1):
        n += 1
        y += 1
        M[x][y] = n
        # NW -> SW
        for i in range(1, c + c):
            n += 1
            x += 1
            M[x][y] = n
        #print(M)
        # SW -> SE
        for i in range(1, 2 * c +1 ):
            n += 1
            y -= 1
            M[x][y] = n
        #print(M)
        # SE -> NE
        for i in range(1, 2 * c + 1):
            n += 1
            x -= 1
            M[x][y] = n
        #print(M)
        # NE -> NW
        for i in range(1, 2 * c + 1):
            n += 1
            y += 1
            M[x][y] = n
        #print(M)

    return M

def sumDiagonal(M):
    s = 0
    l = len(M[0])
    for i in range(l):
        s += M[i][i] + M[i][l - i - 1]
    if l % 2 != 0:
        C = l // 2
        s -= M[C][C]
    return s

print(sumDiagonal(spiral(1001)))
