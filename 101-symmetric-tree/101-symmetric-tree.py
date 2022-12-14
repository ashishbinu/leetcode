# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive
        def is_mirror(left,right):
            if left is None and right is None: return True
            if left is None or right is None: return False
            
            return  left.val == right.val and is_mirror(left.left,right.right) and is_mirror(left.right,right.left)
        
        return root is None or is_mirror(root.left,root.right)
    
        # # time - O(n), space - O(n) - iterative
        # q = deque([root])
        # while q:
        #     pal = []
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         pal.append(node and node.val) # short circuit
        #         if node: q += [node.left,node.right]
        #             
        #     if pal != pal[::-1]: return False
        # return True
    
        # # time - O(n), space - O(n + h) - recursive
        # def dfs(root,res,left):
        #     if root is None: return res.append(None)
        #     res.append(root.val)
        #     if left:
        #         dfs(root.left,res,left)
        #         dfs(root.right,res,left)
        #     else:
        #         dfs(root.right,res,left)
        #         dfs(root.left,res,left)
        #     
        # left = []
        # right = []
        # dfs(root.left,left,True)
        # dfs(root.right,right,False)
        # return left == right