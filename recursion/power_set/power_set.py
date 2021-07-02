def powerset(array):
    # Write your code here.
    rs = [[]]
    for i, n in enumerate(array):
        element = [n]
        rs.append(element)
        new_array = array[i + 1:]
        powerset_helper(new_array, element, rs)
    return rs


def powerset_helper(array, element, rs):
    if not array:
        return
    for i, n in enumerate(array):
        new_element = element[:]
        new_element.append(n)
        rs.append(new_element)
        new_array = array[i + 1:]
        powerset_helper(new_array, new_element, rs)


if __name__ == '__main__':
    array = [1, 2, 3]
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(f"Actual result: {powerset(array)}. Expected: {expected}")
