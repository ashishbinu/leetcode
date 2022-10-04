# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # time - O(height of tree), space - O(1)
        # only works for bst
        
        l,r = (p,q) if p.val < q.val else (q,p)
        while root and not(l.val <= root.val <= r.val):
            root = (root.left,root.right)[root.val < l.val]
        return root
        
        # # this works for binary tree also
        # # time - O(n) , space - O(height of the tree)
        # if root is None: return root
        # if p == root or q == root: return root
        # 
        # left = self.lowestCommonAncestor(root.left,p,q)
        # right = self.lowestCommonAncestor(root.right,p,q)
        # 
        # if right and left: return root
        # 
        # return right or left
        