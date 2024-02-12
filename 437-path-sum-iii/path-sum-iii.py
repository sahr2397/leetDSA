from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, cSum, tSum, pDict):

            if not node : return 0
            
            cSum+=node.val
            diff=cSum-tSum
            res= pDict[diff] 
            pDict[cSum]+=1

            res+=dfs(node.left,cSum,tSum,pDict)
            res+=dfs(node.right,cSum,tSum,pDict)

            pDict[cSum]-=1
            # cSum-=node.val
            return res
            
        pDict=defaultdict(int)
        pDict[0]=1
        
        return dfs(root,0,targetSum,pDict)
        