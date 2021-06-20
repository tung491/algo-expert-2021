def non_constructible_change(coins):
    coins.sort()
    max_created = 0
    for coin in coins:
        if coin > max_created + 1:
            break
        else:
            max_created += coin
    return max_created + 1


if __name__ == '__main__':
    coins = [5, 7, 1, 1, 2, 3, 22]
    expected = 20
    print(f"Actual result: {non_constructible_change(coins)}. "
          f"Expected: {expected}")