from typing import TYPE_CHECKING

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        return self.isSymmetricRec(root.left,root.right)
    def isSymmetricRec(self, nodeL: TreeNode,nodeR: TreeNode) -> bool:
        if not nodeL and not nodeR:
            return True
        elif not nodeL or not nodeR:
            return False
        elif nodeL.val==nodeR.val:
            return self.isSymmetricRec(nodeL.left, nodeR.right) and self.isSymmetricRec(nodeL.right, nodeR.left)
        else:
            return False
'''
Question Type: Tree Recursion
Question Difficulty: Easy
'''