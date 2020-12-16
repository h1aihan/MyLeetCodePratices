import collections
from typing import TYPE_CHECKING
from typing import List
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq=collections.deque()
        dq.append(root)
        result_list=[]
        while(dq):
            this_level=[]
            while(dq):
                this_level.append(dq.popleft())
            for i in this_level:
                if i.left:
                    dq.append(i.left)
                if i.right:
                    dq.append(i.right)
            this_level_val = map(lambda x:x.val, this_level)
            result_list.append(this_level_val)
        return result_list
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        total_List = []
        def levelOrder_rec(root, level, total_List):
            if not root:
                return
            
            if len(total_List) <= level:
                total_List.append([])
            total_List[level].append(root.val)
            levelOrder_rec(root.left, level + 1, total_List)
            levelOrder_rec(root.right, level + 1, total_List)
        levelOrder_rec(root,0,total_List)
        return total_List
        
'''
Question Type: Tree Recursion Queue
Question Difficulty: Medium
'''