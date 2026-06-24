# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val==key:
            if not root.left and not root.right:
                return None

            elif root.left and root.right:
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.right = self.deleteNode(root.right, successor.val)
                
                successor.left = root.left
                successor.right = root.right
                return successor
            
            elif root.left:
                return root.left

            elif root.right:
                return root.right



        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
