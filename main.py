from safe import Safe
import unittest


def processDocument(fileName: str, initialPosition: int):
    safe = Safe(initialPosition)
    zeroCounter = 0
    with open(fileName, "r") as file:
        for line in file:
            # print(f"Direction: {line[0]}, Distance: {line[1:]}")
            if safe.rotateDial(line[0], int(line[1:])):
                zeroCounter += 1
    # print(f"zeroCounter: {zeroCounter}")
    return zeroCounter


class TestProcessDocument(unittest.TestCase):
    def testProcessDocument(self):
        zeroCount = processDocument("input/day1test.txt", 50)
        self.assertEqual(zeroCount, 3)


if __name__ == "__main__":
    # unittest.main()

    # actual work for day1
    zeroCount = processDocument("input/day1.txt", 50)
    print(f"zeroCount: {zeroCount}")
