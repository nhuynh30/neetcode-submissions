# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0

        def recurse(root):
            if not root:
                return -1
            left = recurse(root.left)
            right = recurse(root.right)
            self.maxVal = max(self.maxVal, left+right+2)

            return max(left,right)+1
        
        recurse(root)
        return self.maxVal