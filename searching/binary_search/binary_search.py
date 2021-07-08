def binarySearch(array, target):
    # Write your code here.
    return binary_search_helper(array, target, 0)


def binary_search_helper(array, target, start_idx):
    if not array:
        return -1
    median_idx = len(array) // 2
    median_point = array[median_idx]
    if median_point == target:
        return median_idx + start_idx
    elif median_point < target:
        return binary_search_helper(array[median_idx + 1:], target, median_idx + 1 + start_idx)
    else:
        return binary_search_helper(array[:median_idx], target, start_idx)


if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    expected = 3
    print(f"Actual: {binarySearch(array, target)}. Expected: {expected}")