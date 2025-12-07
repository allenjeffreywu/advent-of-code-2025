import unittest


def readQuestions(fileName: str) -> tuple[list[list[int]], list[str]]:
    numbers = []
    operators = []

    with open(fileName, "r") as file:
        data = file.read().splitlines()
        numProblems = len(data[0].split())
        numRows = len(data) - 1
        numbers = [[0 for _ in range(numRows)] for _ in range(numProblems)]
        for i, arr in enumerate(data[:-1]):
            currArr = arr.split()
            for j, e in enumerate(currArr):
                numbers[j][i] = int(e)
        operators = data[-1].split()

    return numbers, operators


# def readCephalopodNumbers(numbers: list[list[int]]) -> None:
#     numbers[0][0] = 1


def getMathHomeworkAnswers(numbers: list[list[int]], operators: list[str]) -> int:
    runningTotal = 0
    for i in range(len(operators)):
        match operators[i]:
            case '+':
                runningTotal += sum(numbers[i])
            case '*':
                total = 1
                for num in numbers[i]:
                    total *= num
                runningTotal += total

    return runningTotal


class TestMathHomework(unittest.TestCase):
    def testGetMathHomeworkAnswers(self):
        numbers, operators = readQuestions("input/day6test.txt")
        self.assertEqual(getMathHomeworkAnswers(numbers, operators), 4277556)

    # def testGetMathHomeworkAnswersWithCephalopodNumbers(self):
    #     numbers, operators = readQuestions("input/day6test.txt")
    #     numbers = readCephalopodNumbers(numbers)
    #     self.assertEqual(getMathHomeworkAnswers(numbers, operators), 3263827)


if __name__ == "__main__":
    # unittest.main()

    numbers, operators = readQuestions("input/day6test.txt")
    numbers = readCephalopodNumbers(numbers)
    print(getMathHomeworkAnswers(numbers, operators))
