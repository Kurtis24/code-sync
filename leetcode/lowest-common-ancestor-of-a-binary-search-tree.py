# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #if p > q: lower = q , higher = p this is so we can see that if its in them middle
        # and we need to see if there are roots on the left and the right, and so we know what to set it too 
        #since this is a BST what we can do is, make filter right away based on the higher root 
        #find all the nodes 

        curr = root
        if p.val > q.val: 
            higher = p.val
            lower=q.val
        else:
            higher = q.val
            lower=p.val

        while curr: 
            if higher >= curr.val and lower <= curr.val:
                return curr
            elif q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val:
                curr = curr.left