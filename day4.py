import unittest


def readFloor(fileName: str) -> list[list[str]]:
    floor = []
    with open(fileName, "r") as file:
        for line in file:
            currLine = []
            for char in line:
                if char == "\n":
                    continue
                currLine.append(char)
            floor.append(currLine)
    return floor


def checkBoundary(r: int, c: int, floor: list[list[str]]) -> bool:
    MAX_ADJACENT_ROLLS = 4
    directions = [[1, 0], [1, 1], [0, 1], [-1, 1],
                  [-1, 0], [-1, -1], [0, -1], [1, -1]]

    if r == 0:
        directions = list(filter(lambda x: x[0] != -1, directions))
    if c == 0:
        directions = list(filter(lambda x: x[1] != -1, directions))
    if r == len(floor) - 1:
        directions = list(filter(lambda x: x[0] != 1, directions))
    if c == len(floor[0]) - 1:
        directions = list(filter(lambda x: x[1] != 1, directions))
    count = 0
    for dr, dc in directions:
        if floor[r + dr][c + dc] == "@":
            count += 1
        if count >= MAX_ADJACENT_ROLLS:
            return False
    return True


def getRemovableRollLocations(floor: list[list[str]]) -> list[list[int]]:
    ROWS = len(floor)
    COLS = len(floor[0])
    rollLocations = []
    for r in range(ROWS):
        for c in range(COLS):
            if floor[r][c] == "@" and checkBoundary(r, c, floor):
                rollLocations.append([r, c])
    return rollLocations


def getNumberOfAccessibleRolls(floor: list[list[str]]) -> int:
    return len(getRemovableRollLocations(floor))


def removeRolls(floor: list[list[str]], rollLocations=list[list[int]]) -> None:
    for r, c in rollLocations:
        floor[r][c] = "."


def getNumberOfRollsThatCanBeRemoved(floor: list[list[str]]) -> int:
    ROWS = len(floor)
    COLS = len(floor[0])
    totalRollsRemoved = 0

    rollLocations = getRemovableRollLocations(floor)
    while len(rollLocations) > 0:
        totalRollsRemoved += len(rollLocations)
        removeRolls(floor, rollLocations)
        rollLocations = getRemovableRollLocations(floor)
    return totalRollsRemoved


class TestRollsAccessibleByForklift(unittest.TestCase):
    def testGetNumberOfAccessibleRolls(self):
        floor = readFloor("input/day4test.txt")
        self.assertEqual(getNumberOfAccessibleRolls(floor), 13)

    def testGetNumberOfRollsThatCanBeRemoved(self):
        floor = readFloor("input/day4test.txt")
        self.assertEqual(getNumberOfRollsThatCanBeRemoved(floor), 43)


if __name__ == "__main__":
    # unittest.main()

    floor = readFloor("input/day4.txt")
    print("Answer: ", getMaxNumberOfRollsThatCanBeRemoved(floor))
