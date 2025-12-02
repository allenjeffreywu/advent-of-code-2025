import unittest


class Safe:
    SAFE_LEFT_BOUND = 0
    SAFE_RIGHT_BOUND = 99
    SAFE_RANGE = abs(SAFE_RIGHT_BOUND - SAFE_LEFT_BOUND) + 1

    def __init__(self, initialPosition: int):
        assert (Safe.SAFE_LEFT_BOUND <=
                initialPosition and initialPosition <= Safe.SAFE_RIGHT_BOUND)
        self.dialPosition = initialPosition

    def rotateDial(self, direction: str, distance: int):
        assert (distance > Safe.SAFE_LEFT_BOUND)
        assert (direction in ["L", "R"])

        if distance >= Safe.SAFE_RANGE:
            distance %= Safe.SAFE_RANGE
        match direction:
            case "L":
                self.dialPosition -= distance
            case "R":
                self.dialPosition += distance

        if self.dialPosition < Safe.SAFE_LEFT_BOUND:
            self.dialPosition = Safe.SAFE_RIGHT_BOUND + self.dialPosition + 1
        elif self.dialPosition > Safe.SAFE_RIGHT_BOUND:
            self.dialPosition = Safe.SAFE_LEFT_BOUND + \
                (self.dialPosition - Safe.SAFE_RIGHT_BOUND) - 1

        return self.dialPosition == 0


class TestSafe(unittest.TestCase):
    def setUp(self):
        pass

    def testRotateDial_1(self):
        safe = Safe(11)
        self.assertFalse(safe.rotateDial("R", 8))
        self.assertEqual(safe.dialPosition, 19)
        self.assertTrue(safe.rotateDial("L", 19))
        self.assertEqual(safe.dialPosition, 0)

    def testRotateDial_2(self):
        safe = Safe(5)
        self.assertFalse(safe.rotateDial("L", 10))
        self.assertEqual(safe.dialPosition, 95)
        self.assertTrue(safe.rotateDial("R", 5))
        self.assertEqual(safe.dialPosition, 0)


if __name__ == "__main__":
    unittest.main()
