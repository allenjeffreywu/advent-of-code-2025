import unittest


# we can brute force this one, for each cell check all 8 directions. Probably not ideal but it will work
# we can minimize checking by having a sliding window. we ignore the roll at the selected index
# just check all around it

# nah let's just check all around with some bounds checking

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
        # remove all directions that have -1 for r
        directions = list(filter(lambda x: x[0] != -1, directions))
    if c == 0:
        # remove all directions that have -1 for c
        directions = list(filter(lambda x: x[1] != -1, directions))
    if r == len(floor) - 1:
        # remove all directions that have 1 for r
        directions = list(filter(lambda x: x[0] != 1, directions))
    if c == len(floor[0]) - 1:
        # remove all directions that have 1 for c
        directions = list(filter(lambda x: x[1] != 1, directions))
    count = 0
    for dr, dc in directions:
        if floor[r + dr][c + dc] == "@":
            count += 1
        if count >= MAX_ADJACENT_ROLLS:
            return False

    return True


def rollsAccessibleByForkliftP1(floor: list[list[str]]) -> int:
    ROWS = len(floor)
    COLS = len(floor[0])
    totalRollsAccessibleByForklift = 0
    for r in range(ROWS):
        for c in range(COLS):
            if floor[r][c] == "@" and checkBoundary(r, c, floor):
                totalRollsAccessibleByForklift += 1
    return totalRollsAccessibleByForklift


class TestRollsAccessibleByForklift(unittest.TestCase):
    def testRollsAccessibleByForkliftP1(self):
        floor = readFloor("input/day4test.txt")
        self.assertEqual(rollsAccessibleByForkliftP1(floor), 13)


if __name__ == "__main__":
    # unittest.main()

    floor = readFloor("input/day4.txt")
    print("Answer: ", rollsAccessibleByForkliftP1(floor))
