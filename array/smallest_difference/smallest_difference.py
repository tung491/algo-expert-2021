from typing import List


def smallest_difference(array1: List[int], array2: List[int]) -> List[int]:
    array1.sort()
    array2.sort()
    i, j = 0, 0
    min_diff = float('inf')
    result = []
    while i in range(len(array1)) and j in range(len(array2)):
        num1, num2 = array1[i], array2[j]
        diff = num1 - num2
        if abs(diff) < min_diff:
            min_diff = abs(diff)
            result = [num1, num2]
        if diff < 0:
            i += 1
        elif diff > 0:
            j += 1
        else:
            break
    return result


if __name__ == '__main__':
    array1 = [-1, 5, 10, 20, 28, 3]
    array2 = [26, 134, 135, 15, 17]
    expected = [28, 26]
    print(f"Actual result: {smallest_difference(array1, array2)}.\n"
          f"Expected: {expected}")