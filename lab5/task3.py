import math
from numpy import matrix
from functools import reduce


def multiply(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k] * B[k][j]
            result[i].append(sum)
    return result


def transpose(A):
    return list(map(list, zip(*A)))


def build_Hivens(A, i):
    H = eye(len(A))
    theta = math.atan(A[i][i]/A[i+1][i])
    H[i][i] = math.sin(theta)
    H[i][i+1] = math.cos(theta)
    H[i+1][i] = -math.cos(theta)
    H[i+1][i+1] = math.sin(theta)
    return H


def eye(n):
    ls = [[0]*n for _ in range(n)]
    for i in range(n):
        ls[i][i] = 1
    return ls

def add(A, B):
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(len(A)):
            res[i].append(A[i][j] + B[i][j])
    return res

def subtract(A, B):
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(len(A)):
            A[i][j]
            res[i].append(A[i][j] - B[i][j])
    return res


def mult_by_scalar(matr, scalar):
    return list(map(lambda x: [i*scalar for i in x], matr))


def eye_minus_wwt(w):
    e = eye(len(w))
    wwt = multiply(w, transpose(w))
    return subtract(e, mult_by_scalar(wwt, 2))


def build_w(A, col):
    s = 0

    for i in range(col, len(A)-1):
        s += A[i+1][col] ** 2
    s = math.sqrt(s)
    w = []
    for i in range(col+1):
        w.append([0])
    for i in range(col+1, len(A)):
        w.append([A[i][col]])
    w[col+1][0] -= s
    mu = 1/math.sqrt(2 * s * (s - A[col+1][col]))
    return mult_by_scalar(w, mu)


def Householder(A):
    qs = eye(len(A))
    for i in range(len(A)-2):
        w = build_w(A, i)
        qi = eye_minus_wwt(w)
        qs = multiply(qs, transpose(qi))
        A = multiply(qi, A)
        A=multiply(A, qi)
    return A, qs


def Hivens_rotation(A):
    qs = eye(len(A))
    for i in range(len(A)-1):

        H = build_Hivens(A, i)
        A = multiply(H, A)
        qs = multiply(H, qs)

    return A, transpose(qs)

def norm(A):
    s = 0
    for i in range(len(A)):
        s += A[-1][i]**2
    return math.sqrt(s)

def qr_double_shift(A):
    A, qs = Householder(A)
    n = norm(A)
    n2 = 0
    it = 1
    while abs(n2 - n) > 1e-7:
        #if i % 2 == 0:
        n = norm(A)
        k1=A[-1][-1]
        k2=A[-2][-2]
        shift1= mult_by_scalar(eye(len(A)), k1)
        shift2= mult_by_scalar(eye(len(A)), k2)
        A1 = subtract(A, shift1)
        R1, Q1 = Hivens_rotation(A1)
        A2 = multiply(R1, Q1)
        A2 = add(A2, shift1)
        A2 = subtract(A2, shift2)
        R2, Q2 = Hivens_rotation(A2)
        A3 = multiply(R2, Q2)
        A = add(A3, shift2)
        R, Q = Hivens_rotation(A)
        A=multiply(R, Q)
        print()
        print(f"iteration {it}")
        it +=1
        print(matrix(A))
        n2=norm(A)

f = open("matrix.txt")
matr = list(
    map(lambda x: [float(i) for i in x.strip().split()], f.readlines()))
print((matr))
f.close()

qr_double_shift(matr)
