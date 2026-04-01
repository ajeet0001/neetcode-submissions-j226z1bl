# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_so_far):
            if root is None:
                return 0
            count = 0
            if root.val>=max_so_far:
                count = 1
            new_max = max(root.val,max_so_far)
            left = dfs(root.left,new_max)
            right = dfs(root.right,new_max)
            return count+left+right
        return dfs(root,root.val)