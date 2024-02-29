testmatrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

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
    return [matrix]

def round_zero(matrix, tolerance):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) < tolerance:
                matrix[i][j] = 0
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

print_matrix(testmatrix)
print("=========")
[testmatrix, swaps] = elimination(testmatrix)
print_matrix(round_zero(testmatrix, 0.00001))
print("swaps = " + str(swaps))










        
        

        

