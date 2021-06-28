from collections import defaultdict


def min_rewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in range(len(scores) - 2, -1, -1):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)

if __name__ == '__main__':
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    expected = 25
    print(f"Actual result: {min_rewards(scores)}. Expected: {expected}")