def merge_overlapping_intervals(intervals):
    intervals.sort()
    rs = [intervals[0]]
    for interval in intervals:
        last_interval = rs[-1]
        if last_interval[0] <= interval[0] and interval[1] <= last_interval[1]:
            continue
        elif interval[0] <= last_interval[1] < interval[1]:
            overlap_interval = rs.pop()
            rs.append([overlap_interval[0], interval[1]])
        else:
            rs.append(interval)
    return rs


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    expected = [[1, 2], [3, 8], [9, 10]]
    print(f"Actual result: {merge_overlapping_intervals(intervals)}. Expected: {expected}")