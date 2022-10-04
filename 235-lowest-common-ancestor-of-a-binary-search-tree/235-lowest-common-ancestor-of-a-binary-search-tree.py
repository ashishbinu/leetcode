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
        while root:
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val: return root
            root = root.left if p.val < root.val else root.right
        return None
        
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
        