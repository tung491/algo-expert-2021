def two_number_sum(array: list, target_sum: int) -> list:
    # Two pointer approach
    array.sort()
    left_idx, right_idx = 0, len(array) - 1
    while left_idx < right_idx:
        sum_ = array[left_idx] + array[right_idx]
        if sum_ == target_sum:
            return [array[left_idx], array[right_idx]]
        elif sum_ < target_sum:
            left_idx += 1
        else:
            right_idx -= 1
    else:
        return []


if __name__ == '__main__':
    expected = [-1, 11]
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    print(f"Result: {two_number_sum(array, target_sum)}. Expected: {expected}")
