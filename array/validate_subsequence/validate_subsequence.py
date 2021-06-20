def validate_subsequence(array: list, sequence: list) -> bool:
    seq_idx, array_idx = 0, 0
    while seq_idx < len(sequence) and array_idx < len(array):
        if sequence[seq_idx] == array[array_idx]:
            seq_idx += 1
        array_idx += 1
    return seq_idx == len(sequence)


if __name__ == '__main__':
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    expected = True
    print(f"Actual result: {validate_subsequence(array, sequence)}. Expected: {expected}")