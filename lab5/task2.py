import math
from numpy import matrix
from functools import reduce
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

def mult_by_scalar(matr, scalar):
    return list(map(lambda x: [i*scalar for i in x], matr))

def findMax(A):
    max_elem = 0
    max_i = 0
    max_j = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if abs(A[i][j]) >= max_elem:
                max_elem = abs(A[i][j])
                max_i = i
                max_j = j
    return max_i, max_j, max_elem


def rotate(A, i, j):
    phi = 0.5 * math.atan(2 * A[i][j]/(A[i][i] - A[j][j]))
    U = [[0] * len(A) for i in range(len(A))]
    Uinv = [[0] * len(A) for i in range(len(A))]
    for k in range(len(A)):
        U[k][k] = 1
        Uinv[k][k] = 1
    U[i][i] = math.cos(phi)
    U[j][j] = math.cos(phi)
    U[i][j] = math.sin(phi)
    U[j][i] = -math.sin(phi)

    Uinv[i][i] = math.cos(phi)
    Uinv[j][j] = math.cos(phi)
    Uinv[i][j] = -math.sin(phi)
    Uinv[j][i] = math.sin(phi)
    new_A =  multiply(U, A)
    new_A = multiply(new_A, Uinv)
    return new_A, U

#????
def getSum(A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                sum += A[i][j] ** 2
    return sum

def Jacobi(A):
    rotators = []
    iterations = 1
    while findMax(A)[2] > 1e-5:
        print(f"iteration {iterations}")
        iterations +=1 
        i, j, _ = findMax(A)
        new_A, U = rotate(A, i, j)
        rotators.insert(0, U)
        A = new_A
        print(matrix(A))
    fin = reduce(multiply, rotators)
    print(matrix(fin))
    for k in range(len(A)):
      print(f"eigval = {A[k][k]}, eigvec={mult_by_scalar(list(map(lambda x: [x], fin[k])), 1/fin[k][3])}")

f = open("matrix.txt")
matr = list(
    map(lambda x: [float(i) for i in x.strip().split()], f.readlines()))
print(matr)
f.close()

Jacobi(matr)
