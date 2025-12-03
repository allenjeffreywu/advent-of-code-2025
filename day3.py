import unittest


def readBatteryBanks(fileName: str) -> list:
    bankList = []
    with open(fileName, "r") as file:
        bankList = file.read().splitlines()
    return bankList


def convertStringToNumberArray(s: str) -> list:
    num = int(s)
    numArr = []
    while num > 0:
        digit = num % 10
        numArr.insert(0, digit)
        num //= 10
    return numArr


def maxJoltageOfBatteryBanksP1(bankList: list) -> int:
    joltageSum = 0
    for bank in bankList:
        l = 0
        r = 1
        bankNum = convertStringToNumberArray(bank)
        currentMax = int(bank[l] + bank[r])
        rMax = bankNum[r]
        while r < len(bank):
            if bankNum[l] < bankNum[r]:
                currentMax = int(bank[l] + bank[r])
                rMax = 0
                l = r
            elif bankNum[r] > rMax:
                rMax = bankNum[r]
                currentMax = int(bank[l] + bank[r])
            r += 1
        joltageSum += currentMax
    return joltageSum


def getIndexOfLargestDigit(nums: list, start, end) -> int:
    index = -1
    maxDigitVal = -1
    for i in range(start, end, 1):
        if nums[i] > maxDigitVal:
            index = i
            maxDigitVal = nums[i]
    return index


def maxJoltageOfBatteryBanksP2(bankList: list) -> int:
    NUM_BATTERIES = 12
    joltageSum = 0
    for bank in bankList:
        bankNum = convertStringToNumberArray(bank)
        currentJoltage = ""
        l = 0
        r = len(bankNum) - NUM_BATTERIES + 1

        while len(currentJoltage) < NUM_BATTERIES:
            indexOfLargest = getIndexOfLargestDigit(bankNum, l, r)
            currentJoltage += bank[indexOfLargest]
            l = indexOfLargest + 1
            r += 1
            if len(bankNum[l:]) + len(currentJoltage) == NUM_BATTERIES:
                currentJoltage += bank[l:]
                break
        joltageSum += int(currentJoltage)
        print(currentJoltage)
    return joltageSum


class TestMaxJoltageOfBatteryBanks(unittest.TestCase):
    def testMaxJoltageOfBatteryBanksP1(self):
        bankList = readBatteryBanks("input/day3test.txt")
        self.assertEqual(maxJoltageOfBatteryBanksP1(bankList), 357)

    def testMaxJoltageOfBatteryBanksP2(self):
        bankList = readBatteryBanks("input/day3test.txt")
        self.assertEqual(maxJoltageOfBatteryBanksP2(bankList), 3121910778619)


if __name__ == "__main__":
    # unittest.main()

    bankList = readBatteryBanks("input/day3.txt")
    print("Answer: ", maxJoltageOfBatteryBanksP2(bankList))
