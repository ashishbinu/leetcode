# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            if root is None: return None
            if p == root or q == root: return root
            
            right = lca(root.right,p,q)
            left = lca(root.left,p,q)
            
            if right and left: return root
            
            return right or left
        
        return lca(root,p,q)