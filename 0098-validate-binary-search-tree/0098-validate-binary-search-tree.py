# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_list(h):
            ans = []
            def inorder(h):
                if h is None: return 
                inorder(h.left)
                ans.append(h.val)
                inorder(h.right)
                return
            inorder(h)
            return ans
        
        inorder = inorder_list(root)
        print(inorder)
        prev = -math.inf
        for v in inorder:
            if prev >= v: return False
            prev = v
        return True
            
        