# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, subRoot):
            if root is None:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            return check(root.left,subRoot) or check(root.right,subRoot)
        
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if root and not subRoot:
                return False
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right) and root.val==subRoot.val

        return check(root,subRoot)
            

            
            
