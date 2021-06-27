def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return not array[i - 1] <= num <= array[i + 1]


def subarray_sort(array):
    min_out_of_order = float('inf')
    max_out_of_order = float('-inf')
    rs = [-1, -1]
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)

    if min_out_of_order == float('inf'):
        return [-1, -1]

    left_idx, right_idx = 0, len(array) - 1

    while min_out_of_order >= array[left_idx]:
        left_idx += 1

    while max_out_of_order <= array[right_idx]:
        right_idx -= 1
    return [left_idx, right_idx]


if __name__ == '__main__':
    array = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
    expected = [4, 6]
    print(f"Actual result: {subarray_sort(array)}. Expected: {expected}")