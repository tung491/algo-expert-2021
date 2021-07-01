def product_sum(array):
    return product_sum_helper(array, 1)


def product_sum_helper(array, depth):
    sum_ = 0
    for element in array:
        if isinstance(element, int):
            sum_ += element
        else:
            sum_ += (depth + 1) * product_sum_helper(element, depth + 1)
    return sum_


if __name__ == '__main__':
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    expected = 12
    print(f"Actual result: {product_sum(array)}. Expected is {expected}")