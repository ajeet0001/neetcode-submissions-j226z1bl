# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self,root):
        while root.left is not None:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val >key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            # case 1
            if root.left is None and root.right is None:
                return None
            # case 2
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # case 3
            successor = self.findMin(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)
        return root
