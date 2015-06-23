import unittest

from solution import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        start = "hit"
        end = "cog"
        word_dict = ["hot", "dot", "dog", "lot", "log"]
        # "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        self.assertEqual(self.solution.ladderLength(start, end, word_dict), 5)

    def test_none_solution(self):
        start = "hot"
        end = "dog"
        word_dict = ["hot", "dog"]
        self.assertEqual(self.solution.ladderLength(start, end, word_dict), 0)


def test():
    unittest.main()


if __name__ == '__main__':
    test()
