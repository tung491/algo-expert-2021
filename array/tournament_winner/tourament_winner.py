from collections import defaultdict


def tournament_winner(competitions, results):
    competition_result = defaultdict(int)
    for match, result in zip(competitions, results):
        winner = match[result ^ 1]
        competition_result[winner] += 3
    return max(competition_result.items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    competitions = [
      ["HTML", "C#"],
      ["C#", "Python"],
      ["Python", "HTML"]]
    results = [0, 0, 1]
    expected = "Python"
    print(f"Actual result: {tournament_winner(competitions, results)}. "
          f"Expected: {expected}")