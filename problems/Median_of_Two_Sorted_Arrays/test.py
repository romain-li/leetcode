import unittest

from solution import Solution


class TestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testSolution01(self):
        A = (1, 3, 5, 7, 9, 11)
        B = (2, 4, 6, 8, 10)
        self.assertEqual(self.solution.findMedianSortedArrays(A, B), 6)

    def testSolution02(self):
        A = (1, 3, 4, 5, 7, 9, 11)
        B = (2, 6, 8, 10)
        self.assertEqual(self.solution.findMedianSortedArrays(A, B), 6)

    def testSolution03(self):
        A = (1, 2, 3, 4, 5, 9)
        B = (6, 7, 8, 10, 11)
        self.assertEqual(self.solution.findMedianSortedArrays(A, B), 6)

    def testSolution04(self):
        A = (1, 2, 3, 4, 5, 6)
        B = (7, 8, 9, 10, 11)
        self.assertEqual(self.solution.findMedianSortedArrays(A, B), 6)


def test():
    unittest.main()


if __name__ == '__main__':
    test()
