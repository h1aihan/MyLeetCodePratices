from typing import TYPE_CHECKING
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
'''
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # (O(n^2))
        if not root:
            return
        if p.val<q.val:
            left=p
            right=q
        else:
            left=q
            right=p
        if self.isInBetween(root, left, right):
            return root
        else:
            return self.lowestCommonAncestor(root.left,p,q) or self.lowestCommonAncestor(root.right,p,q) 
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(n) official 
        if not root:
            return
        if (root.val <= p.val and root.val>=q.val) or (root.val <= q.val and root.val>=p.val):
            return root
        elif (root.val < p.val and root.val<q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        elif (root.val > p.val and root.val>q.val):
            return self.lowestCommonAncestor(root.left,p,q)
    def isInBetween(self, root: 'TreeNode', left: 'TreeNode', right: 'TreeNode') -> bool:
        isLeft= False
        isRight= False
        if self.isDecendent(root.left, left) or root.val==left.val:
            isLeft=True
        if self.isDecendent(root.right, right) or root.val==right.val:
            isRight= True
        return isLeft and isRight
    def isDecendent(self, root: 'TreeNode', node: 'TreeNode') -> bool:
        if not root:
            return False
        elif root.val==node.val:
            return True
        else:
            return self.isDecendent(root.left,node) or self.isDecendent(root.right, node)
'''
Question Type: Tree Recursion
Question Difficulty: Easy
'''
            