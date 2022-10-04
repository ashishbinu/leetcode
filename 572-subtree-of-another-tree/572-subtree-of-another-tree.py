# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(a,b): # checks if both trees are identical or not
            if a is None and b is None: return True
            if a is None or b is None: return False
            if a.val != b.val: return False
            return is_same(a.left,b.left) and is_same(a.right,b.right)
        
        def is_sub_tree(root,subroot): # checks if the root tree contains subtree
            if is_same(root,subroot): return True
            if root is None: return False
            return is_sub_tree(root.left,subroot) or is_sub_tree(root.right,subroot)
            
        return is_sub_tree(root,subRoot)
        