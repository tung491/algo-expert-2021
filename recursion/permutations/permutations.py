import copy


def get_permuatations(array):
    if not array:
        return []

    current_array = []
    rs = []
    for n in array:
        element = [n]
        popped_array = array[:]
        popped_array.remove(n)
        get_permuatations_helper(rs, popped_array, element)
    return rs


def get_permuatations_helper(rs, array, element):
    if not array:
        rs.append(element)
        return
    for n in array:
        appended_array = element[:]
        appended_array.append(n)
        popped_array = array[:]
        popped_array.remove(n)
        get_permuatations_helper(rs, popped_array, appended_array)


if __name__ == '__main__':
    array = [1, 2, 3]
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(f"Actual result: {get_permuatations(array)}. Expected: {expected}")