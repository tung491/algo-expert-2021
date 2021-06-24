def is_monotonic(array: list) -> bool:
    if len(array) < 2:
        return True
    direction = array[1] - array[0]
    i, j = 1, 2
    while j < len(array):
        if direction == 0:
            direction = array[j] - array[i]
        elif direction > 0 and array[i] > array[j]:
            return False
        elif direction < 0 and array[i] < array[j]:
            return False
        i += 1
        j += 1
    else:
        return True


if __name__ == '__main__':
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    print(f"Acutal result: {is_monotonic(array)}. "
          f"Excepted: {True}")