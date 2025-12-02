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


def findInvalidIdP1(ranges: list) -> int:
    """findInvalidIdP1 takes in a list of ranges and returns the sum of all invalid ids that have 2 repeated sequences

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


def checkInvalidP2(idValue: int) -> bool:
    numDigits = int(math.log10(idValue) + 1)
    idStr = str(idValue)
    for i in range(2, numDigits + 1):
        segmentLength = numDigits / i
        if not segmentLength.is_integer():
            continue
        segmentLength = int(segmentLength)
        j = 0
        while j < numDigits - segmentLength:
            if idStr[j:j + segmentLength] != idStr[j + segmentLength: j + (2 * segmentLength)]:
                break
            # print(
            #     f"first: {idStr[j:j + segmentLength]} second: {idStr[j + segmentLength: j + (2 * segmentLength)]}")
            j += segmentLength
        if j == numDigits - segmentLength:
            return True
    return False


def findInvalidIdP2(ranges: list) -> int:
    """findInvalidIdP1 takes in a list of ranges and returns the sum of all invalid ids that have any number of repeated sequences

    Args:
        ranges (list): list of ranges. Ranges are formatted [begin, end]

    Returns:
        int: sum of all invalid ids
    """
    sumIds = 0
    for b, e in ranges:
        for i in range(b, e + 1):
            if checkInvalidP2(i):
                sumIds += i

    return sumIds


class TestFindInvalidId(unittest.TestCase):
    def testFindInvalidIdP1(self):
        rangeList = processRanges("input/day2test.txt")
        self.assertEqual(findInvalidIdP1(rangeList), 1227775554)

    def testFindINvalidIdP2(self):
        rangeList = processRanges("input/day2test.txt")
        self.assertEqual(findInvalidIdP2(rangeList), 4174379265)


if __name__ == "__main__":
    # unittest.main()

    # actual work for day2 p2
    rangeList = processRanges("input/day2.txt")
    print(findInvalidIdP2(rangeList))
