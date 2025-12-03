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
        # print(currentMax)
        joltageSum += currentMax
    return joltageSum


def getIndexOfLargestDigit(nums: list) -> int:
    index = -1
    maxDigitVal = -1
    for i in range(len(nums)):
        if nums[i] > maxDigitVal:
            index = i
            maxDigitVal = nums[i]
    return index


def maxJoltageOfBatteryBanksP2(bankList: list) -> int:
    # select 12 digits instead of the two
    # ideally select the largest number at each step, but how can we ensure we are selecting the 12 largest numbers each time
    # feels like a greedy problem
    # I want to select the largest and earliest number in a portion of the array
    # first digit comes from max(bank[:-11]). Whatever that index is, we then select on the rest of the array
    # if the amount of digits == the size of the array, then we select the rest of the array.

    pass


class TestMaxJoltageOfBatteryBanks(unittest.TestCase):
    def testMaxJoltageOfBatteryBanksP1(self):
        bankList = readBatteryBanks("input/day3test.txt")
        self.assertEqual(maxJoltageOfBatteryBanksP1(bankList), 357)

    # def testMaxJoltageOfBatteryBanksP2(self):
    #     bankList = readBatteryBanks("input/day3test.txt")
    #     self.assertEqual(maxJoltageOfBatteryBanksP2(bankList), 3121910778619)


if __name__ == "__main__":
    unittest.main()
    # bankList = readBatteryBanks("input/day3test.txt")
    # print(maxJoltageOfBatteryBanksP1(bankList))
    # nums = convertStringToNumberArray(bankList[1])
    # print(nums, getIndexOfLargestDigit(nums))
    # print(convertStringToNumberArray("1000"))
