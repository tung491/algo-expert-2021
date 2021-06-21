def move_element_to_end(array, to_move):
    i, j = 0, len(array) - 1
    for _ in range(len(array)):
        if array[i] == to_move:
            array[i], array[j] = array[j], array[i]
            j -= 1
        else:
            i += 1
    return array


if __name__ == '__main__':
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    expected = [4, 1, 3, 2, 2, 2, 2, 2]
    print(f"Actual result: {move_element_to_end(array, to_move)}.\n"
          f"Expected result: {expected}")

