import unittest
import math
from collections import defaultdict


def readJunctionBoxLocations(fileName: str) -> list[tuple[int]]:
    junctionBoxLocations = []

    with open(fileName, "r") as file:
        data = file.read().splitlines()
        for line in data:
            x, y, z = map(lambda x: int(x), line.split(","))
            junctionBoxLocations.append((x, y, z))

    return junctionBoxLocations


def euclideanDistance(pt1: list[int], pt2: list[int]) -> int:
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 + (pt1[2] - pt2[2]) ** 2)


def addJunctionBoxesToCircuits(a: tuple[int], b: tuple[int], circuits: list[set[tuple[int]]], visited: set[tuple[int]]) -> int:
    if a in visited and b in visited:
        aCircuit = set()
        bCircuit = set()
        for c in circuits:
            if a in c:
                aCircuit = c
                circuits.remove(c)
                break
        for c in circuits:
            if b in c:
                bCircuit = c
                circuits.remove(c)
                break
        circuits.append(aCircuit.union(bCircuit))
    elif a in visited and b not in visited:
        for c in circuits:
            if a in c:
                c.add(b)
                break
    elif b in visited and a not in visited:
        for c in circuits:
            if b in c:
                c.add(a)
                break
    else:
        circuits.append(set([a, b]))
    visited.add(a)
    visited.add(b)


def connectJunctionBoxesP1(junctionBoxes: list[tuple[int]], numConnections: int) -> int:
    NUM_BOXES = len(junctionBoxes)

    distanceMap = defaultdict(list)  # key: distance, value: coordinate pairs

    # calculate all distances
    for i in range(NUM_BOXES):
        for j in range(i + 1, NUM_BOXES):
            distance = euclideanDistance(junctionBoxes[i], junctionBoxes[j])
            distanceMap[distance].append([junctionBoxes[i], junctionBoxes[j]])

    # connect the numConnections shortest distances
    shortestDistances = sorted(distanceMap.keys())

    visited = set()
    circuits = []
    for i in range(numConnections):
        for a, b in distanceMap[shortestDistances[i]]:
            addJunctionBoxesToCircuits(a, b, circuits, visited)

    # get their lengths and calculate final answer
    circuitLengths = sorted(
        list(map(lambda x: len(x), circuits)), reverse=True)

    res = 1

    for i in range(3):
        res *= circuitLengths[i]

    return res


class TestJunctionBoxConnections(unittest.TestCase):
    def testConnectJunctionBoxesP1(self):
        junctionBoxes = readJunctionBoxLocations("input/day8test.txt")
        self.assertEqual(connectJunctionBoxesP1(junctionBoxes, 10), 40)


if __name__ == "__main__":
    # unittest.main()

    junctionBoxes = readJunctionBoxLocations("input/day8.txt")
    print("Answer: ", connectJunctionBoxesP1(junctionBoxes, 1000))
