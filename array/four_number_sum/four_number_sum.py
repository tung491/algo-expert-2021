from collections import defaultdict

def four_number_sum(array, target_sum):
    rs = []
    pair_sum = defaultdict(list)
    for i in range(1 , len(array) - 1):
        for j in range(i + 1, len(array)):
            sub_num = target_sum - array[i] - array[j]
            if sub_num in pair_sum:
                for pair in pair_sum[sub_num]:
                    rs.append([*pair, array[i], array[j]])
        for k in range(i):
            pair_sum[array[i] + array[k]].append([array[k], array[i]])
    return rs


if __name__ == '__main__':
    array = [7, 6, 4, -1, 1, 2]
    target_sum = 16
    expected = [[7, 6, 4, -1], [7, 6, 1, 2]]
    print(f"Actual result: {four_number_sum(array, target_sum)}. Expected: {expected}")