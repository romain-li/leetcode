import unittest

from solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_solution2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('bbbbb'), 1)

    def test_solution3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring('abcabcdefabcdefg'), 7)


def test():
    unittest.main()


if __name__ == '__main__':
    test()
