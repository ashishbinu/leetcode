# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(a,b):
            if a is None and b is None: return True
            return a and b and a.val == b.val and is_same(a.left,b.left) and is_same(a.right,b.right)
        
        def is_sub_tree(root,subroot):
            return is_same(root,subroot) or (root and (is_sub_tree(root.left,subroot) or is_sub_tree(root.right,subroot)))
                
            
        return is_sub_tree(root,subRoot)
        