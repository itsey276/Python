A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 2], [2, 2, 1], [2, 3, 1]]

def mmult(A, B):
    m = len(A)
    n = len(B[0])
    if len(A[0]) != len(B):
        raise Exception("Matrix dimension mismatch")
    C = [ [0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def transpose(A):
    C = []
    m = len(A)
    n = len(A[0])
    for i in range(n):
        R = []
        for j in range(m):
            R.append(A[j][i])
        C.append(R)
    return C

def append(A, B):
    C = []
    m = len(A)
    if len(A) != len(B):
        raise Exception("Row mismatch error")
    for i in range(m):
        C.append(A[i] + B[i])
    return C

def mprint(A):
    for i in range(len(A)):
        print(A[i])

def reduce_row(k, l, matrix):
    for i in range(k + 1, len(matrix)):
        factor = matrix[i][l] / matrix[k][l]
        for j in range(l, len(matrix[0])):
            matrix[i][j] = matrix[i][j] - factor * matrix[k][j]
    return matrix

def elimination(matrix):
    k = 0
    l = 0
    while k < len(matrix) and l < len(matrix[0]):
        if matrix[k][l] != 0:
            matrix = reduce_row(k, l, matrix)
            k += 1
            l += 1
        else:
            l += 1
    return matrix

def round_zero(matrix, tolerance):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) < tolerance:
                matrix[i][j] = 0
    return matrix

def Graham_Schmidt(A):
    P = append(mmult(A, transpose(A)), A)
    elimination(P)
    round_zero(P, 0.0001)
    return P

mprint(Graham_Schmidt(A))
