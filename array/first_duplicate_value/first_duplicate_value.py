def first_duplicate_value(array):
    # Write your code here.
    for i, n in enumerate(array):
        abs_n = abs(n)
        if array[abs_n - 1] < 0:
            return abs_n
        else:
            array[abs_n - 1] *= -1
    return -1


if __name__ == '__main__':
    array = [2, 1, 5, 2, 3, 3, 4]
    expected = 2
    print(f"Actual result: {first_duplicate_value(array)}. Expected: {expected}")
