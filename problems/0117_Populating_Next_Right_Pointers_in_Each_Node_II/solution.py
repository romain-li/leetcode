# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        if root.left and root.right:
            root.left.next = root.right

        if root.next and (root.left or root.right):
            next = root.next
            while (next and not next.left and not next.right):
                next = next.next

            if next:
                last = root.right if root.right else root.left
                last.next = next.left if next.left else next.right

        self.connect(root.right)
        self.connect(root.left)
