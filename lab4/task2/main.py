import math


def f1(x, y):
    return math.tan(x * y + 0.571) - x**2


def df1dx(x, y):
    return y/math.cos(x * y + 0.571)**2 - 2 * x


def df2dx(x, y):
    return 1.12 * x


def f2(x, y):
    return 0.56 * x * x - 1.587 * y * y - 1


def df1dy(x, y):
    return x/math.cos(x * y + 0.571)**2


def df2dy(x, y):
    return 3.174 * y


def norm(x, y):
    return math.sqrt(x*x + y*y)


def add(v1, v2):
    n = []
    for i in range(len(v1)):
        n.append(v1[i] + v2[i])
    return n


def subtract(v1, v2):
    n = []
    for i in range(len(v1)):
        n.append(v1[i] - v2[i])
    return n


def multiply(matr, vec):
    n = []
    for i in range(2):
        val = 0
        for j in range(2):
            val += matr[i][j] * vec[j]
        n.append(val)
    return n


def det(matr):
    return matr[0][0] * matr[1][1] - matr[1][0] * matr[0][1]


def invert(matr):
    deter = det(matr)
    return [[matr[1][1]/deter, -matr[0][1]/deter], [-matr[1][0]/deter, matr[0][0]/deter]]


# ============first root==================
print("===============root 1==================")
x = [1.5, 0.4]
Finv = invert([[df1dx(*x), df1dy(*x)], [df2dx(*x), df2dy(*x)]])
print(f"x={x}")
print(f"finv={Finv}")
nev_norm = 1000000000  # magic value
it = 0
while nev_norm >= 1e-5:
    it += 1
    print(f"iteration {it}")
    print(f"new value = {x}")
    x = subtract(x, multiply(Finv, [f1(*x), f2(*x)]))
    
    Finv = invert([[df1dx(x[0], x[1]), df1dy(x[0], x[1])], [df2dx(x[0], x[1]), df2dy(x[0], x[1])]])
    nev_norm = norm(f1(x[0], x[1]), f2(x[0], x[1]))
    print(f"residual norm = {nev_norm}")
    print()

xfinal1 = x
# =========================================

# ============second root================
print("===============root 2==================")
x = [-1.5, -0.45]
Finv = invert([[df1dx(*x), df1dy(*x)], [df2dx(*x), df2dy(*x)]])
print(f"x={x}")
print(f"finv={Finv}")
nev_norm = 1000000000  # magic value
it = 0
while nev_norm >= 1e-5:
    it += 1
    print(f"iteration {it}")
    print(f"new value = {x}")
    x = subtract(x, multiply(Finv, [f1(x[0], x[1]), f2(x[0], x[1])]))

    Finv = invert([[df1dx(x[0], x[1]), df1dy(x[0], x[1])], [df2dx(x[0], x[1]), df2dy(x[0], x[1])]])
    nev_norm = norm(f1(x[0], x[1]), f2(x[0], x[1]))
    print(f"residual norm = {nev_norm}")
    print()

xfinal2 = x
# ========================================
