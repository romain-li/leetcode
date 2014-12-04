import unittest
import Queue

from solution import Solution
from models import TreeNode


class TestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def _testSolution(self, deep):
        node_count = pow(2, deep)
        node_queue = Queue.Queue(node_count)
        root_queue = Queue.Queue(node_count / 2)

        # Generate the tree
        nodes = [TreeNode(x) for x in xrange(1, node_count)]
        root_queue.put(nodes[0])
        for node in nodes[1:]:
            node_queue.put(node)

        while(not node_queue.empty()):
            root = root_queue.get()
            root.left = node_queue.get()
            root.right = node_queue.get()
            root_queue.put(root.left)
            root_queue.put(root.right)

        # Solution
        self.solution.connect(nodes[0])

        # Assertion
        for level in xrange(deep):
            self.assertLinkedList(nodes[pow(2, level) - 1], pow(2, level))

    def assertLinkedList(self, root, length):
        count = 0
        # linked_list = []
        while (root):
            # linked_list.append(str(root.val))
            root = root.next
            count += 1
        # print ' -> '.join(linked_list)
        self.assertEqual(count, length)


# Add some auto generate test case
def test(deep):
    def _test(self):
        self._testSolution(deep)
    return _test

for deep in xrange(1, 15):
    setattr(TestCase, 'testDeep%.2d' % deep, test(deep))


def test():
    unittest.main()


if __name__ == '__main__':
    test()
