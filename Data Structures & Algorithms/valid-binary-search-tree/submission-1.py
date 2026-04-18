# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bts(root, minval, maxval):
            if not root:
                return True
            left = bts(root.left, minval, root.val)
            right = bts(root.right, root.val, maxval)
            if root.val <= minval or root.val>=maxval:
                return False
            return left and right
        return bts(root, float("-inf"), float("inf"))
        