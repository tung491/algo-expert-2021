def zigzag_traversal(array):
    rs = []
    x, y = 0, 0
    x_min, y_min = 0, 0
    x_max = len(array)
    y_max = len(array[0])

    # top left to top righ
    goingDown = True
    while x in range(x_min, x_max) and y in range(y_min, y_max):
        rs.append(array[x][y])
        if goingDown:
            if y == 0 or x == len(array) - 1:
                if x == len(array) - 1:
                    y += 1
                else:
                    x += 1
                goingDown = False
            else:
                x += 1
                y -= 1
        else:
            if x == 0 or y == len(array[0]) - 1:
                if y == len(array[0]) - 1:
                    x += 1
                else:
                    y += 1
                goingDown = True
            else:
                x -= 1
                y += 1
    return rs


if __name__ == '__main__':
    array = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]
    expected = list(range(1, 17))
    print(f"The actual result: {zigzag_traversal(array)}. Expected: {expected}")
