import unittest
from collections import deque


def readManifold(fileName: str) -> tuple[list[list[str]], list[int]]:
    manifold = []
    start = None
    with open(fileName, "r") as file:
        data = file.read().splitlines()
        for r in range(len(data)):
            currentLine = []
            for c in range(len(data[r])):
                if data[r][c] == "S":
                    start = [r, c]
                currentLine.append(data[r][c])
            manifold.append(currentLine)
    return manifold, start


def countBeamSplits(manifold: list[list[str]], start: list[int]) -> int:
    ROWS = len(manifold)
    COLS = len(manifold[0])
    numberOfSplits = 0
    queue = deque()
    visited = set()
    queue.append([start[0] + 1, start[1]])
    while queue:
        r, c = queue.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if manifold[r][c] == "^":
            numberOfSplits += 1
            if c + 1 < COLS and r < ROWS - 1:
                queue.append([r + 1, c + 1])
            if c - 1 >= 0 and r < ROWS - 1:
                queue.append([r + 1, c - 1])
        elif r < ROWS - 1:
            queue.append([r + 1, c])

    return numberOfSplits


def countTimeLines(manifold: list[list[str]], start: list[int]) -> int:
    return -1


class TestManifold(unittest.TestCase):
    def testCountBeamSplits(self):
        manifold, start = readManifold("input/day7test.txt")
        self.assertEqual(countBeamSplits(manifold, start), 21)


if __name__ == "__main__":
    # unittest.main()

    manifold, start = readManifold("input/day7.txt")
    print("Answer: ", countBeamSplits(manifold, start))
