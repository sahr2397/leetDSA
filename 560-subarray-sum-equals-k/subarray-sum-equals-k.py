from collections import defaultdict 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pDict=defaultdict(int)
        pDict[0]=1
        pSum=0
        res=0
        for n in nums:
            pSum+=n
            res+= pDict[pSum-k] if pDict[pSum-k] else 0
            pDict[pSum]+=1

        return res





        