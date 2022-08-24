# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # still not tail recursion I think
        def maxdepth(root,d):
            if root is None: return d
            return max(maxdepth(root.left,d+1),maxdepth(root.right,d+1))
        return maxdepth(root,0)
            
        # not tail recursion
        # if root is None: return 0
        # return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))
        