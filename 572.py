from typing import TYPE_CHECKING
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(s*t)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isTheSameTree(s,t):
            return True
        elif not s:
            return False
        else:
            return self.isSubtree(s.right,t) or self.isSubtree(s.left, t)
    def isTheSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return s.val==t.val and self.isTheSameTree(s.left,t.left) and self.isTheSameTree(s.right,t.right)
'''
Question Type: Tree Recursion
Question Difficulty: Easy
'''