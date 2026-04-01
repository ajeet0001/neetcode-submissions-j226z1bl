# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # MY SOLUTION
        # res = []
        # def dfs(root):
        #     if root is None:
        #         return
        #     res.append(root.val)
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        # dfs(root)
        # res.sort()
        # return res[k-1]

        # OPTIMIZED APP
        s = []
        curr = root
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right