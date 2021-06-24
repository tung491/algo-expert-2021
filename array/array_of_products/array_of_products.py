def array_of_products(array: list) -> list:
    prods = [1] * len(array)
    for i in range(1, len(array)):
        prods[i] = prods[i - 1] * array[i - 1]

    right_prod = 1
    for i in range(len(array) - 1, -1, -1):
        prods[i] *= right_prod
        right_prod *= array[i]
    return prods


if __name__ == '__main__':
    array = [5, 1, 4, 2]
    expected = [8, 40, 10, 20]
    print(f"Actual result: {array_of_products(array)}. Expected: {expected}")