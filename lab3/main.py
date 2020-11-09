import math


def prepare_for_iterations(matr, answers):
    for i in range(5):
        answers[i] /= matr[i][i]
        for j in range(5):
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
    for i in range(5):
        s = 0
        for j in range(5):
            s += matr[i][j] * vec[j]
        res.append(s)
    return res


def multiply_matrix(matr1, matr2):
    res = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                res[i][j] += matr1[i][k] * matr2[k][j]
    return res


def transpose(matr):
    res = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            res[i][j] = matr[j][i]
    return res


def norm(vec):
    res = 0
    for i in vec:
        res += i**2
    return math.sqrt(res)


matr = []
f = open("file.txt")
for _ in range(5):
    matr.append(list(map(float, f.readline().strip().split())))

ans = []
for _ in range(5):
    ans.append(float(f.readline()))

ans = multiply(transpose(matr), ans)
matr = multiply_matrix(transpose(matr), matr)

matr2 = []
for i in range(5):
    matr2.append(matr[i][::])
ans2 = ans[::]
prepare_for_iterations(matr2, ans2)
solution = [0] * 5
nev_norm = 100000000 #magic don`t touch

iterations = 0
while nev_norm > 1e-5:
    iterations += 1
    print(f"iteration: {iterations}")
    solution = add(multiply(matr2, solution), ans2)
    print(solution)
    print("nevyazka")
    nev = subtract(ans, multiply(matr, solution))
    print(nev)
    nev_norm = norm(nev)
    print(f"norm = {nev_norm}")
