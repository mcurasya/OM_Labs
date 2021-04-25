from numpy import matrix
import math
size = int(input("enter size of a vector >>> "))

def prepare_for_iterations(matr, answers):
    for i in range(size):
        answers[i] /= matr[i][i]
        for j in range(size):
            if i == j:
                continue
            matr[i][j] /= -matr[i][i]
        matr[i][i] = 0


def add(vec1, vec2):
    vec = []
    for i in range(len(vec1)):
        vec.append(vec1[i] + vec2[i])
    return vec


def subtract(vec1, vec2):
    vec = []
    for i in range(len(vec1)):
        vec.append(vec1[i] - vec2[i])
    return vec


def multiply(matr, vec):
    res = []
    for i in range(len(vec)):
        s = 0
        for j in range(len(vec)):
            s += matr[i][j] * vec[j]
        res.append(s)
    return res


def multiply_matrix(matr1, matr2):
    res = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += matr1[i][k] * matr2[k][j]
    return res


def transpose(matr):
    res = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            res[i][j] = matr[j][i]
    return res


def norm(vec):
    res = 0
    for i in vec:
        res += i**2
    return math.sqrt(res)


matr = []
f = open("file.txt")
for _ in range(size):
    matr.append(list(map(float, f.readline().strip().split())))

ans = []
for _ in range(size):
    ans.append(float(f.readline()))


matr2 = []
for i in range(size):
    matr2.append(matr[i][::])
ans2 = ans[::]
prepare_for_iterations(matr2, ans2)

print(matrix(matr2))
print(matrix(ans2).T)

solution = [0] * size
nev_norm = 100000000 #magic don`t touch

iterations = 0
while nev_norm > 1e-6:
    iterations += 1
    print(f"iteration: {iterations}")
    solution = add(multiply(matr2, solution), ans2)
    print(matrix(solution).T)
    print("Residual")
    nev = subtract(ans, multiply(matr, solution))
    print(nev)
    nev_norm = norm(nev)
    print(f"Residual norm = {nev_norm}")
