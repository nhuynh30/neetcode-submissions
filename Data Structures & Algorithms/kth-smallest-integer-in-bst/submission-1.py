# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        def bst(root):
            if not root:
                return 
            root.left = bst(root.left)
            self.arr.append(root.val)
            root.right = bst(root.right)

        bst(root)
        return self.arr[k-1]