import numpy as np


def printMatr(_matr):
    for row in _matr:
        row = np.array(row)
    _matr = np.array(_matr)
    print(_matr)


def multiplyArrays(arr1, arr2):
    matrix = np.zeros((len(arr1), len(arr2)), dtype=float)
    ll = list(matrix)
    for l in ll:
        l = list(l)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            ll[i][j] = arr1[i] * arr2[j]
    return ll


def findMaxInArr(arr):
    _max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > _max:
            _max = arr[i]
    return _max


def findMinInArr(_arr):
    if len(_arr) == 0:
        return -1
    _min = _arr[0]
    for i in range(1, len(_arr)):
        if _arr[i] < _min:
            _min = _arr[i]
    return _min


def maxToMin(matr):
    for i in range(len(matr)):
        _max = findMaxInArr(matr[i])
        for j in range(len(matr[i])):
            matr[i][j] -= _max
            matr[i][j] *= -1
    return matr


def reduceByMinRow(matr):
    for i in range(len(matr)):
        _min = findMinInArr(matr[i])
        for j in range(len(matr[i])):
            matr[i][j] -= _min
    return matr


def minRow(matr):
    min_in_col = []
    for k in range(len(matr[0])):
        min_in_col.append(matr[0][k])
    for i in range(1, len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] < min_in_col[j]:
                min_in_col[j] = matr[i][j]
    return min_in_col


def reduceByMinCol(matr):
    _min = minRow(matr)
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            matr[i][j] -= _min[j]
    return matr


def stepOne(matr):
    return reduceByMinCol(reduceByMinRow(matr))


def stepTwo(matr, c):
    interim_matrix = []
    l = 0
    n = len(matr)
    count_zeros_cols = np.zeros(n)
    count_zeros_rows = np.zeros(n)
    for i in range(n):
        interim_matrix.append([])
        for j in range(n):
            if matr[i][j] == 0:
                interim_matrix[i].append(1)
                count_zeros_cols[j] += 1
                count_zeros_rows[i] += 1
            else:
                interim_matrix[i].append(0)
    row_indexes = [i for i in range(n)]
    col_indexes = [i for i in range(n)]

    res_rows = []
    res_cols = []

    while sum(count_zeros_rows) + sum(count_zeros_cols) > 0:

        redundant_cols = []
        for k in col_indexes:
            if count_zeros_cols[k] == findMinInArr([x for x in count_zeros_cols if x > 0]):
                redundant_cols.append(k)
        for i in redundant_cols:
            if count_zeros_cols[i] > 0:
                redundant_rows = []
                for j in row_indexes:
                    if interim_matrix[j][i] == 1:
                        redundant_rows.append(j)
                _max = count_zeros_rows[redundant_rows[0]]
                row_index = redundant_rows[0]
                for k in redundant_rows:
                    if count_zeros_rows[k] > _max:
                        _max = count_zeros_rows[k]
                        row_index = k
                for k in [x for x in col_indexes if interim_matrix[row_index][x] == 1]:
                    count_zeros_cols[k] -= 1
                res_cols.append(i)
                res_rows.append(row_index)
                count_zeros_rows[row_index] = 0
                count_zeros_cols[i] = 0
                row_indexes.remove(row_index)
                l += 1
            else:
                continue

        redundant_rows = []
        for k in row_indexes:
            if count_zeros_rows[k] == findMinInArr([x for x in count_zeros_rows if x > 0]):
                redundant_rows.append(k)
        for i in redundant_rows:
            if count_zeros_rows[i] > 0:
                redundant_cols = []
                for j in col_indexes:
                    if interim_matrix[i][j] == 1:
                        redundant_cols.append(j)
                _max = count_zeros_cols[redundant_cols[0]]
                col_index = redundant_cols[0]
                for k in redundant_cols:
                    if count_zeros_cols[k] > _max:
                        _max = count_zeros_cols[k]
                        col_index = k
                for k in [x for x in row_indexes if interim_matrix[x][col_index] == 1]:
                    count_zeros_rows[k] -= 1
                res_rows.append(i)
                res_cols.append(col_index)
                count_zeros_cols[col_index] = 0
                count_zeros_rows[i] = 0
                col_indexes.remove(col_index)
                l += 1
            else:
                continue

    if l == n:
        stepThree(res_rows, res_cols)
    else:
        _min = matr[row_indexes[0]][col_indexes[0]]
        for i in row_indexes:
            for j in col_indexes:
                if matr[i][j] < _min:
                    _min = matr[i][j]
        for i in range(n):
            for j in range(n):
                if i not in row_indexes:
                    if j not in col_indexes:
                        matr[i][j] += _min
                    else:
                        continue
                else:
                    if j in col_indexes:
                        matr[i][j] -= _min
                    else:
                        continue
        _c = c + _min * (n - l)
        print('Преобразование:')
        printMatr(matr)
        print('==================')
        print('c = ' + str(_c))
        print('==================')
        stepTwo(matr, _c)


def stepThree(rows, cols):
    res = np.zeros((len(rows), len(cols)), dtype=int)
    ll = list(res)
    for l in ll:
        l = list(l)
    for i in range(len(rows)):
        ll[rows[i]][cols[i]] = 1

    print('X: ')
    printMatr(ll)


solveAsMin = True

# Matrix = multiplyArrays(
#     list([5.72, 7, 6.92, 4.8, 5]),
#     list([0.75, 1.12, 0.55, 1.32, 0.5, 0.45]))

Matrix = [[2, 0, 0, 0, 0, 0],
          [0, 0, 3, 3, 7, 3],
          [0, 3, 5, 1, 0, 4],
          [0, 2, 2, 4, 6, 2],
          [0, 0, 2, 6, 3, 5],
          [1, 1, 4, 2, 1, 0]]

print('Исходная матрица:')
printMatr(Matrix)

if not solveAsMin:
    Matrix = maxToMin(Matrix)

n = len(Matrix)
m = len(Matrix[0])

while n != m:
    if n > m:
        for arr in Matrix:
            arr.append(0)
    else:
        pt = []
        for k in range(m):
            pt.append(0)
        Matrix.append(pt)
    n = len(Matrix)
    m = len(Matrix[0])

c = sum([findMinInArr(Matrix[i]) for i in range(len(Matrix))]) + sum(minRow(reduceByMinRow(Matrix)))
print('==================')
print('c = ' + str(c))
print('==================')
Matrix = stepOne(Matrix)
printMatr(Matrix)
print('==================')
stepTwo(Matrix, c)
