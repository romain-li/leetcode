import unittest

from solution import Solution
from models import ListNode


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertListNodeEqual(self, l1, l2):
        if l1 is None and l2 is None:
            return
        self.assertEqual(l1.val, l2.val)
        self.assertListNodeEqual(l1.next, l2.next)

    def test_factory(self):
        l = ListNodeFactory.create(1, 2, 3)
        self.assertEqual(l.val, 1)
        self.assertEqual(l.next.val, 2)
        self.assertEqual(l.next.next.val, 3)

    def test_solution1(self):
        l1 = ListNodeFactory.create(2, 4, 3)
        l2 = ListNodeFactory.create(5, 6, 4)
        answer = self.solution.addTwoNumbers(l1, l2)
        self.assertListNodeEqual(answer, ListNodeFactory.create(7, 0, 8))

    def test_solution2(self):
        l1 = ListNodeFactory.create(1, 2, 3, 4, 5)
        l2 = ListNodeFactory.create(9, 8, 7, 6, 5, 4)
        answer = self.solution.addTwoNumbers(l1, l2)
        self.assertListNodeEqual(answer, ListNodeFactory.create(0, 1, 1, 1, 1, 5))

    def test_solution2(self):
        l1 = ListNodeFactory.create(5)
        l2 = ListNodeFactory.create(5)
        answer = self.solution.addTwoNumbers(l1, l2)
        self.assertListNodeEqual(answer, ListNodeFactory.create(0, 1))


class ListNodeFactory(object):
    @staticmethod
    def create(*vals):
        last = None
        for val in reversed(vals):
            current = ListNode(val)
            current.next = last
            last = current
        return last


def test():
    unittest.main()


if __name__ == '__main__':
    test()
