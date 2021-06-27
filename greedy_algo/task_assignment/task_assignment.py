def task_assignment(k, tasks):
    tasks = sorted(list(enumerate(tasks)), key=lambda x: x[1])
    tasks1, tasks2 = tasks[:k], tasks[k:][::-1]
    result = []

    for task1, task2 in zip(tasks1, tasks2):
        result.append([task1[0], task2[0]])
    return result


if __name__ == '__main__':
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]
    expected = [
        [0, 2],
        [4, 5],
        [1, 3]
    ]

    print(f"Actual result: {task_assignment(k, tasks)}. Expected: {expected}")