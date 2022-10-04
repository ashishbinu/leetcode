# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # returns the lca if p and q exists and if both doesn't exist in tree then return null
        def lca(root,p,q):
            if root is None: return None
            if p == root or q == root: return root
            
            right = lca(root.right,p,q)
            left = lca(root.left,p,q)
            
            # if p and q are in different subtrees (right or left), so lca is root
            if right and left: return root
            
            # if both p and q are in either right or left
            return right or left
        
        return lca(root,p,q)