# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fn(root,x):
            if root and x == root.val and root.left is None and root.right is None: return True
            if root is None: return False
            return fn(root.left,x-root.val) or fn(root.right,x-root.val)
        
        return fn(root,targetSum)