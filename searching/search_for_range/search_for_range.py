def searchForRange(array, target):
    # Write your code here.
    result_range = [-1, -1]
    search_for_range_helper(array, target, 0, len(array) - 1, result_range, True)
    search_for_range_helper(array, target, 0, len(array) - 1, result_range, False)
    return result_range


def search_for_range_helper(array, target, left, right, result_range, go_left):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] < target:
        search_for_range_helper(array, target, mid + 1, right, result_range, go_left)
    elif array[mid] > target:
        search_for_range_helper(array, target, left, mid - 1, result_range, go_left)
    else:
        if go_left:
            if mid == 0 or array[mid - 1] != target:
                result_range[0] = mid
            else:
                search_for_range_helper(array, target, left, mid - 1, result_range, go_left)
        else:
            if mid == len(array) - 1 or array[mid + 1] != target:
                result_range[1] = mid
            else:
                search_for_range_helper(array, target, mid + 1, right, result_range, go_left)


if __name__ == '__main__':
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45
    expected = [4, 9]
    print(f"Actual result: {searchForRange(array, target)}. Expected: {expected}")