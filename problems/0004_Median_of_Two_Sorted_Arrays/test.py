import unittest

from solution import Solution


class TestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSolution01(self):
        a = (1, 3, 5, 7, 9, 11)
        b = (2, 4, 6, 8, 10)
        self.assertEqual(self.solution.findMedianSortedArrays(a, b), 6)

    def testSolution02(self):
        a = (1, 3, 4, 5, 7, 9)
        b = (2, 6, 8, 10)
        self.assertEqual(self.solution.findMedianSortedArrays(a, b), 5.5)

    def testSolution03(self):
        a = (1, 2, 3, 4, 5, 9)
        b = (6, 7, 8, 10, 11)
        self.assertEqual(self.solution.findMedianSortedArrays(a, b), 6)

    def testSolution04(self):
        a = (1, 2, 3, 4, 5, 6)
        b = (7, 8, 9, 10, 11)
        self.assertEqual(self.solution.findMedianSortedArrays(a, b), 6)

    def testSolution05(self):
        a = (1, 4, 8, 9, 10, 11)
        b = (2, 3, 5, 6, 7)
        self.assertEqual(self.solution.findMedianSortedArrays(a, b), 6)


def test():
    unittest.main()


if __name__ == '__main__':
    test()
