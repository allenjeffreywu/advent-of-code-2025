import unittest
from collections import deque, defaultdict


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


def getBeamSplits(manifold: list[list[str]], start: list[int]) -> list[list[int]]:
    ROWS = len(manifold)
    COLS = len(manifold[0])
    splitLocations = []
    queue = deque()
    visited = set()
    queue.append([start[0] + 1, start[1]])
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        if manifold[r][c] == "^":
            splitLocations.append([r, c])
            if c + 1 < COLS and r < ROWS - 1:
                queue.append([r + 1, c + 1])
            if c - 1 >= 0 and r < ROWS - 1:
                queue.append([r + 1, c - 1])
        elif r < ROWS - 1:
            queue.append([r + 1, c])

    return splitLocations


def countTimeLines(manifold: list[list[str]], start: list[int], splitLocations: list[list[int]]) -> int:
    locations = splitLocations.copy()
    locations.append(start)
    locations.sort(reverse=True)
    queue = deque(locations)
    # intuition is that each split means 2 timelines
    timeLines = defaultdict(lambda: 2)
    while queue:
        r, c = queue.popleft()

        if r == len(manifold) - 2:
            timeLines[(r, c)] = 2

        for nr, nc in queue:
            if nc == c:
                break
            if nc == c - 1 or nc == c + 1:
                # intuition is that we are only adding to one side, we have not calculated the other
                # if this happens a second time, then the original count of 2 timelines is completely
                # replaced by our calculations.
                timeLines[(nr, nc)] += timeLines[(r, c)] - 1

    return timeLines[(start[0], start[1])]


class TestManifold(unittest.TestCase):
    def testCountBeamSplits(self):
        manifold, start = readManifold("input/day7test.txt")
        self.assertEqual(len(getBeamSplits(manifold, start)), 21)

    def testCountTimeLines(self):
        manifold, start = readManifold("input/day7test.txt")
        splitLocations = getBeamSplits(manifold, start)
        self.assertEqual(countTimeLines(manifold, start, splitLocations), 40)


if __name__ == "__main__":
    # unittest.main()

    manifold, start = readManifold("input/day7.txt")
    splitLocations = getBeamSplits(manifold, start)

    print("Answer: ", countTimeLines(manifold, start, splitLocations))
