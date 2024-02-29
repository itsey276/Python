testmatrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]

def swap(a, b, matrix):
    for j in range(len(matrix[0])):
        [matrix[a][j], matrix[b][j]] = [matrix[b][j], matrix[a][j]]
    return matrix

def max_pivot(k, l, matrix):
    max_value = matrix[k][l]
    max_row = k
    for i in range(k + 1, len(matrix)):
        if matrix[i][l] > max_value:
            max_value = matrix[i][l]
            max_row = i
    return max_row

def reduce_row(k, l, matrix):
    for i in range(k + 1, len(matrix)):
        factor = matrix[i][l] / matrix[k][l]
        for j in range(l, len(matrix[0])):
            matrix[i][j] = matrix[i][j] - factor * matrix[k][j]
    return matrix

def elimination(matrix):
    k = 0
    l = 0
    swaps = 0
    while k < len(matrix) and l < len(matrix[0]):
        maxRow = max_pivot(k, l, matrix)
        if maxRow > k:
            matrix = swap(k, maxRow, matrix)
            swaps += 1
        if matrix[k][l] != 0:
            matrix = reduce_row(k, l, matrix)
            k += 1
            l += 1
        else:
            l += 1
    return [matrix, swaps]

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










        
        

        

