import unittest


def getDatabaseData(fileName: str) -> tuple[list[list[int]], list[int]]:
    freshIngredientRanges = []
    ingredientIds = []
    with open(fileName, "r") as file:
        data = file.read().splitlines()
        freshIngredientRangesFinished = False
        for line in data:
            if line == '':
                freshIngredientRangesFinished = True
            elif not freshIngredientRangesFinished:
                freshIngredientRanges.append([int(x) for x in line.split("-")])
            else:
                ingredientIds.append(int(line))
    freshIngredientRanges.sort(key=lambda x: x[0])
    ingredientIds.sort()

    # combine ranges
    tempRanges = [freshIngredientRanges[0]]
    for i in range(1, len(freshIngredientRanges)):
        if tempRanges[-1][1] >= freshIngredientRanges[i][0]:
            tempRanges[-1][1] = max(freshIngredientRanges[i]
                                    [1], tempRanges[-1][1])
        else:
            tempRanges.append(freshIngredientRanges[i])
    freshIngredientRanges = tempRanges

    return freshIngredientRanges, ingredientIds


def getNumFreshIngredients(freshIngredientRanges: list[list[int]], ingredientIds: list[int]) -> int:
    numFreshIngredients = 0
    rangeIdx = 0
    for ingredient in ingredientIds:
        while ingredient > freshIngredientRanges[rangeIdx][1] and rangeIdx < len(freshIngredientRanges) - 1:
            rangeIdx += 1
        if freshIngredientRanges[rangeIdx][0] <= ingredient and ingredient <= freshIngredientRanges[rangeIdx][1]:
            numFreshIngredients += 1
    return numFreshIngredients


def getNumFreshIds(freshIngredientRanges: list[list[int]]) -> int:
    numFreshIds = 0
    for beginning, end in freshIngredientRanges:
        numFreshIds += end - beginning + 1
    return numFreshIds


class TestGetNumFreshIngredients(unittest.TestCase):
    def testGetNumFreshIngredients(self):
        freshIngredientRanges, ingredientIds = getDatabaseData(
            "input/day5test.txt")
        self.assertEqual(getNumFreshIngredients(
            freshIngredientRanges, ingredientIds), 3)

    def testGetNumFreshIds(self):
        freshIngredientRanges, _ = getDatabaseData(
            "input/day5test.txt")
        self.assertEqual(getNumFreshIds(freshIngredientRanges), 14)


if __name__ == "__main__":
    # unittest.main()

    freshIngredientRanges, ingredientIds = getDatabaseData(
        "input/day5.txt")
    print("Answer: ", getNumFreshIds(freshIngredientRanges))
