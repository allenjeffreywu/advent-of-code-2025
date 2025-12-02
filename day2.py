import unittest
import math


def processRanges(fileName: str) -> list:
    result = []
    with open(fileName, "r") as file:
        line = file.read()
        ranges = line.split(",")
        for r in ranges:
            rangeValues = r.split("-")
            begin = int(rangeValues[0])
            end = int(rangeValues[1])
            result.append([begin, end])
            # print(f"begin: {begin}, end: {end}")
    return result


def findInvalidId(ranges: list) -> int:
    """findInvalidId takes in a list of ranges and returns the sum of all invalid ids

    Args:
        ranges (list): list of ranges. Ranges are formatted [begin, end]

    Returns:
        int: sum of all invalid ids
    """
    sumIds = 0
    for b, e in ranges:
        for i in range(b, e + 1):
            # quick check to see if the number in the range is even
            # if it is odd, it cannot have some sequence of digits repeated twice
            numDigits = int(math.log10(i) + 1)
            if numDigits % 2 == 0:
                # we now know it is even, can iterate through left and right pointers
                l = 0
                r = numDigits // 2
                num = str(i)
                while r < numDigits:
                    if num[l] != num[r]:
                        break
                    l += 1
                    r += 1
                if r == numDigits:
                    sumIds += i
    return sumIds


class TestFindInvalidId(unittest.TestCase):
    def testFindInvalidId(self):
        rangeList = processRanges("input/day2test.txt")
        self.assertEqual(findInvalidId(rangeList), 1227775554)


if __name__ == "__main__":
    # unittest.main()
    # actual work for day2 p1
    rangeList = processRanges("input/day2.txt")
    print(findInvalidId(rangeList))
