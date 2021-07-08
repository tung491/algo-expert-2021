def searchInSortedMatrix(matrix, target):
    # Write your code here.
    n, m = len(matrix), len(matrix[0])
    if target < matrix[0][0] or target > matrix[n - 1][m - 1]:
        return [-1, -1]
    i, j = 0, m - 1
    while i in range(n) and j in range(m):
        value = matrix[i][j]
        if value == target:
            return [i, j]
        elif value > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]


if __name__ == '__main__':
    array = [[1, 4, 7, 12, 15, 1000],
             [2, 5, 19, 31, 32, 1001],
             [3, 8, 24, 33, 35, 1002],
             [40, 41, 42, 44, 45, 1003],
             [99, 100, 103, 106, 128, 1004]]
    target = 44
    expected = [3, 3]
    print(f"Actual: {searchInSortedMatrix(array, target)}. Expected: {expected}")
