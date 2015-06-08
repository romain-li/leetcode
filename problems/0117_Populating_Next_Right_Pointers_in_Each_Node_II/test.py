import unittest
import Queue

from solution import Solution
from models import TreeNode


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case01(self):
        self._testSolution(
            (3, 6, 7),
            ((1, 1), (2, 1), (4, 2))
        )

    def test_case02(self):
        self._testSolution(
            (2, 4, 5, 7),
            ((1, 1), (3, 1), (6, 1))
        )

    def test_case03(self):
        self._testSolution(
            (4, 7),
            ((1, 1), (2, 2), (5, 2))
        )

    def test_case04(self):
        self._testSolution(
            (5, 6),
            ((1, 1), (2, 2), (4, 2))
        )

    def test_case05(self):
        self._testSolution(
            (5,),
            ((1, 1), (2, 2), (4, 3))
        )

    def test_case06(self):
        self._testSolution(
            (6, 9, 10, 11, 12, 13, 14),
            ((1, 1), (2, 2), (4, 3), (8, 2)),
            4
        )

    def test_case07(self):
        self._testSolution(
            (9, 10, 11, 12, 13, 14),
            ((1, 1), (2, 2), (4, 4), (8, 2)),
            4
        )

    def _testSolution(self, skip=(), assertions=(), deep=3):
        node_count = pow(2, deep)
        node_queue = Queue.Queue(node_count)
        root_queue = Queue.Queue(node_count / 2)

        # Generate the tree
        nodes = [TreeNode(x) for x in xrange(1, node_count)]
        root_queue.put(nodes[0])
        for node in nodes[1:]:
            node_queue.put(node)

        while not node_queue.empty():
            root = root_queue.get()
            root.left = node_queue.get()
            root.right = node_queue.get()
            root_queue.put(root.left)
            root_queue.put(root.right)

            if root.left.val in skip:
                root.left = None
            if root.right.val in skip:
                root.right = None

        # Solution
        self.solution.connect(nodes[0])

        # Assertion
        for node, length in assertions:
            self.assertLinkedList(nodes[node - 1], length)

    def assertLinkedList(self, root, length):
        count = 0
        linked_list = []
        while root:
            linked_list.append(str(root.val))
            root = root.next
            count += 1
        print ' -> '.join(linked_list)
        self.assertEqual(count, length)


def test():
    unittest.main()


if __name__ == '__main__':
    test()
