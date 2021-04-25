import math
from numpy import matrix
from functools import reduce


def scalar_mult(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i][0] * y[i][0]
    return sum


def add(v1, v2):
    res = []
    for i in range(len(v1)):
        res.append([])
        for j in range(len(v1[0])):
            res[i].append(v1[i][j] + v2[i][j])
    return res


def subtract(v1, v2):
    res = []
    for i in range(len(v1)):
        res.append([])
        for j in range(len(v1[0])):
            res[i].append(v1[i][j] - v2[i][j])
    return res


def transpose(A):
    return list(map(list, zip(*A)))


def mult_by_const(A, alpha):
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(len(A[0])):
            res[i].append(alpha * A[i][j])
    return res


def norm(v):
    res = 0
    for i in v:
        res += i[0]**2
    return math.sqrt(res)


def multiply(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A)):
            sum = 0
            for k in range(len(A)):
                sum += A[i][k] * B[k][j]
            result[i].append(sum)
    return result


def get_vector_col(A, i):
    a = []
    for j in range(len(A)):
        a.append([A[j][i]])
    return a


def project(e, a):
    coeff = scalar_mult(e, a)/scalar_mult(e, e)
    return mult_by_const(e, coeff)


def merge_lists(A, u):
    for i in range(len(A)):
        A[i].append(u[i][0])


def Gramm_Smidt(A):
    U = [[] for _ in A]
    for i in range(len(A)):
        a = get_vector_col(A, i)
        for j in range(len(U[0])):
            uj = get_vector_col(U, j)
            a = subtract(a, project(uj, a))
        merge_lists(U, a)
    E = [[] for _ in A]
    for i in range(len(U)):
        uj = get_vector_col(U, i)
        merge_lists(E, mult_by_const(uj, 1/norm(uj)))
    R=multiply(transpose(E), A)
    return (E, R)

def matr_norm(A):
    s = 0
    for i in range(len(A)):
        s += A[-1][i]**2
    return math.sqrt(s)

def qr_double_shift(A):
    n = matr_norm(A)
    n2 = 0
    it = 1
    while abs(n2 - n) > 1e-7:
        n = matr_norm(A)
        Q, R = Gramm_Smidt(A)
        A=multiply(R, Q)
        print()
        print(f"iteration {it}")
        it += 1
        print(matrix(A))
        print()
        n2 = matr_norm(A)



f = open("matrix.txt")
matr = list(
    map(lambda x: [float(i) for i in x.strip().split()], f.readlines()))
print(matrix(matr))
f.close()

qr_double_shift(matr)
