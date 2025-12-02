from safe import Safe
import unittest


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
    # unittest.main()

    # actual work for day1 p2
    zeroCount = processDocument("input/day1.txt", 50)
    print(f"zeroCount: {zeroCount}")
