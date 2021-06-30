def get_nth_fib(n):
    memoize = {1: 0, 2: 1}
    return get_nth_fib_helper(n, memoize)


def get_nth_fib_helper(n, memoize):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_nth_fib_helper(n - 1, memoize) + get_nth_fib_helper(n - 2, memoize)
        return memoize[n]


if __name__ == '__main__':
    n = 6
    expected = 5
    print(f"Actual result: {get_nth_fib(n)}. Expected: {expected}")