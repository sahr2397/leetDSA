# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,Gval):
            if not node: return 0

            res = 1 if node.val>=Gval else 0

            Gval=max(node.val,Gval)
            res+=dfs(node.left, Gval)
            res+=dfs(node.right,Gval)

            return res

        return dfs(root,root.val)
        
