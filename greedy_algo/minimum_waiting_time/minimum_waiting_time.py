from typing import List


def minimum_waiting_time(queries: List[int]):
    queries.sort()
    rs = 0
    for i, query in enumerate(queries[:-1], start=1):
        rs += query * (len(queries) - i)
    return rs


if __name__ == '__main__':
    queries = [3, 2, 1, 2, 6]
    expected = 17

    print(f"Actual result: {minimum_waiting_time(queries)}. Expected: {expected}")