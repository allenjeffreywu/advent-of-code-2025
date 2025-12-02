import unittest


class Safe:
    SAFE_LEFT_BOUND = 0
    SAFE_RIGHT_BOUND = 99
    SAFE_RANGE = abs(SAFE_RIGHT_BOUND - SAFE_LEFT_BOUND) + 1

    def __init__(self, initialPosition: int):
        assert (Safe.SAFE_LEFT_BOUND <=
                initialPosition and initialPosition <= Safe.SAFE_RIGHT_BOUND)
        self.dialPosition = initialPosition

    def rotateDial(self, direction: str, distance: int):
        assert (distance > Safe.SAFE_LEFT_BOUND)
        assert (direction in ["L", "R"])

        startedAtZero = self.dialPosition == 0
        clicksPastZero = 0
        if distance >= Safe.SAFE_RANGE:
            clicksPastZero += distance // Safe.SAFE_RANGE
            distance %= Safe.SAFE_RANGE
        match direction:
            case "L":
                self.dialPosition -= distance
            case "R":
                self.dialPosition += distance

        if self.dialPosition < Safe.SAFE_LEFT_BOUND:
            self.dialPosition = Safe.SAFE_RIGHT_BOUND + self.dialPosition + 1
            if not startedAtZero:
                clicksPastZero += 1
        elif self.dialPosition > Safe.SAFE_RIGHT_BOUND:
            self.dialPosition = Safe.SAFE_LEFT_BOUND + \
                (self.dialPosition - Safe.SAFE_RIGHT_BOUND) - 1
            if not startedAtZero:
                clicksPastZero += 1
        elif self.dialPosition == 0 and not startedAtZero:
            clicksPastZero += 1

        # we are now counting any click that causes the dial to point to 0
        return clicksPastZero


class TestSafe(unittest.TestCase):
    def setUp(self):
        pass

    def testRotateDial_1(self):
        safe = Safe(11)
        self.assertEqual(safe.rotateDial("R", 8), 0)
        self.assertEqual(safe.dialPosition, 19)
        self.assertEqual(safe.rotateDial("L", 19), 1)
        self.assertEqual(safe.dialPosition, 0)

    def testRotateDial_2(self):
        safe = Safe(5)
        self.assertEqual(safe.rotateDial("L", 10), 1)
        self.assertEqual(safe.dialPosition, 95)
        self.assertEqual(safe.rotateDial("R", 5), 1)
        self.assertEqual(safe.dialPosition, 0)


def processDocument(fileName: str, initialPosition: int):
    safe = Safe(initialPosition)
    zeroCounter = 0
    with open(fileName, "r") as file:
        for line in file:
            zeroCounter += safe.rotateDial(line[0], int(line[1:]))
            # print(
            #     f"Direction: {line[0]}, Distance: {line[1:]} ZeroCounter: {zeroCounter}")
    # print(f"zeroCounter: {zeroCounter}")
    return zeroCounter


class TestProcessDocument(unittest.TestCase):
    def testProcessDocument(self):
        zeroCount = processDocument("input/day1test.txt", 50)
        self.assertEqual(zeroCount, 6)


if __name__ == "__main__":
    unittest.main()

    # actual work for day1 p2
    # zeroCount = processDocument("input/day1.txt", 50)
    # print(f"zeroCount: {zeroCount}")
