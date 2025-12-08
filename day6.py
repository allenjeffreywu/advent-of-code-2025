import unittest


def readQuestions(fileName: str) -> tuple[list[list[str]], list[str]]:
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
                numbers[j][i] = e
        operators = data[-1].split()

    return numbers, operators


def readCephalopodQuestions(fileName: str) -> tuple[list[list[str]], list[str]]:
    numbers = []
    operators = []

    with open(fileName, "r") as file:
        # process operators
        data = file.read().splitlines()
        operatorIndecies = []
        for i, e in enumerate(data[-1]):
            if e != ' ':
                operatorIndecies.append(i)
                operators.append(e)

        # process numbers
        NUMBERS_PER_PROBLEM = len(data) - 1

        for i in range(len(operatorIndecies)):
            j = operatorIndecies[i]
            numsInProblem = []
            if i == len(operatorIndecies) - 1:
                while j < len(data[0]):
                    currentNum = ""
                    for k in range(NUMBERS_PER_PROBLEM):
                        currentNum += data[k][j]
                    j += 1
                    numsInProblem.append(currentNum)
            else:
                while j < operatorIndecies[i + 1] - 1:
                    currentNum = ""
                    for k in range(NUMBERS_PER_PROBLEM):
                        currentNum += data[k][j]
                    j += 1
                    numsInProblem.append(currentNum)
            numbers.append(numsInProblem)
    return numbers, operators


def getMathHomeworkAnswers(numbers: list[list[str]], operators: list[str]) -> int:
    runningTotal = 0
    for i in range(len(operators)):
        match operators[i]:
            case '+':
                total = 0
                for num in numbers[i]:
                    total += int(num)
                runningTotal += total
            case '*':
                total = 1
                for num in numbers[i]:
                    total *= int(num)
                runningTotal += total

    return runningTotal


class TestMathHomework(unittest.TestCase):
    def testGetMathHomeworkAnswers(self):
        numbers, operators = readQuestions("input/day6test.txt")
        self.assertEqual(getMathHomeworkAnswers(numbers, operators), 4277556)

    def testGetMathHomeworkAnswersWithCephalopodNumbers(self):
        numbers, operators = readCephalopodQuestions("input/day6test.txt")
        self.assertEqual(getMathHomeworkAnswers(numbers, operators), 3263827)


if __name__ == "__main__":
    # unittest.main()
    numbers, operators = readCephalopodQuestions("input/day6.txt")
    print(getMathHomeworkAnswers(numbers, operators))
