from collections import defaultdict

def largest_range(array):
    n_dict = defaultdict(bool)
    visited = defaultdict(bool)
    longest_len = float('-inf')
    for n in array:
        n_dict[n] = True

    longest_range = []
    for n in array:
        if visited[n]:
            continue

        left = n
        right = n
        while n_dict[left-1]:
            visited[left - 1] = True
            left -= 1

        while n_dict[right + 1]:
            visited[right + 1] = True
            right += 1
        len_ = right - left + 1
        if len_ > longest_len:
            longest_len = len_
            longest_range = [left, right]
    return longest_range


if __name__ == '__main__':
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    expected = [0, 7]
    print(f"Actual result: {largest_range(array)}. Expected: {expected}")