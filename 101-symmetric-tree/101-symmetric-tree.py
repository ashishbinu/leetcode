# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            pal = []
            for i in range(len(q)):
                node = q.popleft()
                pal.append(node.val if node else None)
                if node:
                    q.append(node.left)
                    q.append(node.right)
            if pal != pal[::-1]: return False
        return True