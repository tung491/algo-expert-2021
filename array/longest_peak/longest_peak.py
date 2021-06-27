def longest_peak(array):
    start_peak = 0
    longest_peak = 0
    i = 0
    while i in range(len(array) - 2):
        n1 = array[i]
        n2 = array[i + 1]
        n3 = array[i + 2]
        incr_trend = n1 < n2
        if n2 > n1 and n2 > n3:  # is peak
            y, z = i + 2, i + 3
            while z < len(array):
                if array[y] > array[z]:  # descr trend
                    y += 1
                    z += 1
                else:
                    break
            peak_len = y - start_peak + 1
            longest_peak = max(longest_peak, peak_len)
        if not incr_trend:
            start_peak = i + 1
        i += 1
    return longest_peak


if __name__ == '__main__':
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    expected = 6
    print(f"Actual result: {longest_peak(array)}. Expected: {expected}")