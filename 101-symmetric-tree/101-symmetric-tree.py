# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,res,left):
            if root is None: return res.append(None)
            res.append(root.val)
            if left:
                dfs(root.left,res,left)
                dfs(root.right,res,left)
            else:
                dfs(root.right,res,left)
                dfs(root.left,res,left)
            
        left = []
        right = []
        dfs(root.left,left,True)
        dfs(root.right,right,False)
        return left == right
            
            
        # time - O(n), space - O(n)
        # q = deque([root])
        # while q:
        #     pal = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         pal.append(node.val if node else None)
        #         if node:
        #             q.append(node.left)
        #             q.append(node.right)
        #     if pal != pal[::-1]: return False
        # return True