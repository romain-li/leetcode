TITLE = 'Binary Tree Inorder Traversal'
ADD_DATE = '2012-08-27'
DIFFICULTY = 'Medium'
URL = 'https://oj.leetcode.com/problems/binary-tree-inorder-traversal/'
BOOK = False
PROBLEM = r"""Given a binary tree, return the _inorder_ traversal of its nodes' values.

For example:  
Given binary tree `{1,#,2,3}`,  

    
    
    
       1
        \
         2
        /
       3
    

return `[1,3,2]`.

**Note:** Recursive solution is trivial, could you do it iteratively?

confused what `"{1,#,2,3}"` means? > read more on how binary tree is
serialized on OJ.

  
**OJ's Binary Tree Serialization:**

The serialization of a binary tree follows a level order traversal, where '#'
signifies a path terminator where no node exists below.

Here's an example:  

    
    
    
       1
      / \
     2   3
        /
       4
        \
         5
    

The above binary tree is serialized as `"{1,2,3,#,#,4,#,#,5}"`.


"""
