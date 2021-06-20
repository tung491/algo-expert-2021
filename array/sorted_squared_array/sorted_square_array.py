def sorted_squared_array(array: list) -> list:
    left_idx, right_idx = 0, len(array) - 1
    rs = [None] * len(array)
    for idx in range(len(array) - 1, -1, -1):
        left_n, right_n = array[left_idx], array[right_idx]
        squared_left, squared_right = left_n ** 2, right_n ** 2
        if squared_left > squared_right:
            rs[idx] = squared_left
            left_idx += 1
        else:
            rs[idx] = squared_right
            right_idx -= 1
    return rs


if __name__ == '__main__':
    array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
    expected = sorted([n ** 2 for n in array])
    print(f"Actual result: {sorted_squared_array(array)}."
          f" Expected: {expected}")
