# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(node):
            L= getDepth(node.left) if node.left!=None else 0
            R= getDepth(node.right) if node.right!=None else 0
            
            return 1+max(L,R)

        return getDepth(root) if root else 0
        