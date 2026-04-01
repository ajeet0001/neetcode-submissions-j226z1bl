# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return (0,0)
            rob_left , skip_left = dfs(root.left)
            rob_right, skip_right = dfs(root.right)
            rob = root.val + skip_left + skip_right
            skip = max(rob_left,skip_left)  + max(rob_right, skip_right)
            return (rob,skip)
        return max(dfs(root))