def indexEqualsValue(array):
    # Write your code here.
    for i, n in enumerate(array):
        if i == n:
            return i
    else:
        return -1


if __name__ == '__main__':
    array = [-5, -3, 0, 3, 4, 5, 9]
    expected = 3
    print(f"Actual: {indexEqualsValue(array)}. Expected: {expected}")