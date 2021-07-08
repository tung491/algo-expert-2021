def findThreeLargestNumbers(array):
    # Write your code here.
    maxs = sorted(array[:3])
    for n in array[3:]:
        if n < maxs[0]:
            continue
        elif n in range(maxs[0], maxs[1]):
            maxs[0] = n
        elif n in range(maxs[1], maxs[2]):
            maxs = [maxs[1], n, maxs[2]]
        elif n > maxs[2]:
            maxs = [*maxs[1:3], n]
    return maxs


if __name__ == '__main__':
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    expected = [18, 141, 541]
    print(f"Actual: {findThreeLargestNumbers(array)}. Expected: {expected}")