import unittest

from solution import Solution


class TestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSolutionr1(self):
        self.assertEqual(self.solution.twoSum((2, 7, 11, 15), 9), (1, 2))

    def testSolution2(self):
        self.assertEqual(self.solution.twoSum((0, 4, 3, 0), 0), (1, 4))


def test():
    unittest.main()


if __name__ == '__main__':
    test()
