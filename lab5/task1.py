import math


def transpose(m):
    return list(map(list, zip(*m)))


def getMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def det(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*det(getMinor(m, 0, c))
    return determinant


def Invert(m):
    determinant = det(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * det(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def mult_by_scalar(matr, scalar):
    return list(map(lambda x: [i*scalar for i in x], matr))


def multiply(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A)):
                sum += A[i][k] * B[k][j]
            result[i].append(sum)
    return result


def subtract(x, y):
    res = []
    for i in range(len(x)):
        res.append([x[i][0] - y[i][0]])
    return res


def scalar(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i][0] * y[i][0]
    return sum


f = open("matrix.txt")
matr = list(
    map(lambda x: [float(i) for i in x.strip().split()], f.readlines()))
print(matr)
f.close()

print("max eigvalue")
lambd = float("inf")
vec = [[1] for _ in matr]
i = 0
while True:
    new_vec = multiply(matr, vec)
    new_lambd = scalar(new_vec, new_vec)/scalar(vec, new_vec)

    vec = mult_by_scalar(new_vec, 1/scalar(new_vec, new_vec))
    nev = subtract(multiply(matr, vec), mult_by_scalar(vec, new_lambd))
    i += 1
    print(f"iteration {i}")
    print(f"new lambda = {new_lambd}")
    print(f"new vector = {vec}")
    print(f"residual = {nev}")
    print(f"residual norm = {math.sqrt(scalar(nev, nev))}")
    if math.sqrt(scalar(nev, nev)) < 1e-5:
        lambd = new_lambd
        break
    lambd = new_lambd

max_lambda = lambd
max_vec = vec[::]

print("min eigvalue")
i = 0
matr2 = Invert(matr)
lambd = float("inf")
vec = [[1] for _ in matr2]
while True:
    new_vec = multiply(matr2, vec)
    new_lambd = scalar(new_vec, new_vec)/scalar(vec, new_vec)
    print(new_lambd)
    vec = mult_by_scalar(new_vec, 1/scalar(new_vec, new_vec))
    nev = subtract(multiply(matr, vec), mult_by_scalar(vec, 1/new_lambd))
    print(nev)
    print(math.sqrt(scalar(nev, nev)))
    i += 1
    print(f"iteration {i}")
    print(f"new lambda = {new_lambd}")
    print(f"new vector = {vec}")
    print(f"residual = {nev}")
    print(f"residual norm = {math.sqrt(scalar(nev, nev))}")
    if math.sqrt(scalar(nev, nev)) < 1e-5:
        lambd = new_lambd
        break
    lambd = new_lambd

min_lambda = 1/lambd
min_vec = vec[::]
print(f"max eigenvalue={max_lambda}\nmin eigenvalue={min_lambda}")

print(
    f"max eigenvector={mult_by_scalar(max_vec, 1/max_vec[3][0])}\nmin eigenvector={mult_by_scalar(min_vec, 1/min_vec[3][0])}")
nev = subtract(multiply(matr, max_vec), mult_by_scalar(max_vec, max_lambda))
print(
    f"nevyazka for max vector = {nev}\nnev_norm={math.sqrt(scalar(nev, nev))}")
nev = subtract(multiply(matr, min_vec), mult_by_scalar(min_vec, min_lambda))
print(
    f"nevyazka for min vector = {nev}\nnev_norm={math.sqrt(scalar(nev, nev))}")
