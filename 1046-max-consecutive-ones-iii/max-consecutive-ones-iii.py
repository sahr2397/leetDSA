class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=end=0
        n=len(nums)
        maxLen=0

        zcount=0

        while(end<n):
            num=nums[end]

            if num==0: 
                zcount+=1

            if zcount>k:
                while(nums[start]!=0):
                    start+=1
                zcount-=1
                start+=1
            maxLen=max(maxLen,end-start+1)
   
            end+=1

        return maxLen
