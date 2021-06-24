def spiral_traverse(array: list) -> list:
    x_start, x_end = 0, len(array) - 1
    y_start, y_end = 0, len(array[0]) - 1
    result = []
    x, y = 0, 0
    element_n = len(array) * len(array[0])

    while len(result) < element_n:
        for y in range(y_start, y_end + 1):
            result.append(array[x][y])
        if len(result) == element_n:
            break
        x_start += 1
        for x in range(x_start, x_end + 1):
            result.append(array[x][y])
        if len(result) == element_n:
            break
        y_end -= 1

        for y in range(y_end, y_start - 1, -1):
            result.append(array[x][y])
        x_end -= 1
        if len(result) == element_n:
            break

        for x in range(x_end, x_start - 1, -1):
            result.append(array[x][y])
        y_start += 1
    return result


if __name__ == '__main__':
    array = [[1, 2, 3, 4],
             [12, 13, 14, 5],
             [11, 16, 15, 6],
             [10, 9, 8, 7]]
    print(spiral_traverse(array))
