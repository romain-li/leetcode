import unittest

from solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.longestPalindrome('abcdcbabc'), 'abcdcba')
        self.assertEqual(self.solution.longestPalindrome('ddabccbaa'), 'abccba')
        self.assertEqual(self.solution.longestPalindrome('abcbabcba'), 'abcbabcba')
        self.assertEqual(self.solution.longestPalindrome('z' * 1000), 'z' * 1000)



def test():
    unittest.main()


if __name__ == '__main__':
    test()
