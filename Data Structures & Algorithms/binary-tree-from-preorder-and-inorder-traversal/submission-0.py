# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 and len(preorder)==0:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val) # construct tree node 
        # fin index of the root value in inorder
        idx = inorder.index(root_val)
        # using array seperate inorder list in left sub tree or right sub tree nodes
        left_inorder = inorder[:idx]
        right_inorder = inorder[idx+1:len(inorder)]

        # do same for preorder list as well
        left_pre = preorder[1:len(left_inorder)+1]
        right_pre = preorder[len(left_inorder)+1:len(preorder)]
        root.left = self.buildTree(left_pre,left_inorder)
        root.right = self.buildTree(right_pre,right_inorder)
        return root