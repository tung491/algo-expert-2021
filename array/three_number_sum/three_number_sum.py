def three_number_sum(array, target):
    array.sort()
    result = []
    for idx1, num1 in enumerate(array):
        remain_target = target - num1
        idx2, idx3 = idx1 + 1, len(array) - 1
        while idx2 < idx3:
            num2, num3 = array[idx2], array[idx3]
            two_number_sum = num2 + num3
            if two_number_sum < remain_target:
                idx2 += 1
            elif two_number_sum > remain_target:
                idx3 -= 1
            else:
                result.append([num1, num2, num3])
                idx2 += 1
                idx3 -= 1
    return result


if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(f"Acutal result: {three_number_sum(array, target)}\n"
          f"Expected: {expected}")