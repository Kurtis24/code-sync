# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:           # both None
            return True
        if not p or not q:            # one is None
            return False
        
        return (
        p.val == q.val
        and self.isSameTree(p.left, q.left)
        and self.isSameTree(p.right, q.right)
    )        #breath first search, this function allows you, go through all the branch ane it checks if it is equal