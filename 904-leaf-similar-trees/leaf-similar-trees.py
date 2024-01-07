# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(n):
            if n==None: return []
            if n.left==None and n.right==None:
                return [n.val]
            
            return [*getLeaves(n.left)]+[*getLeaves(n.right)]

        tree1Leaves=getLeaves(root1)
        tree2Leaves=getLeaves(root2)

        return tree1Leaves==tree2Leaves
