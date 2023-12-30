class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxLen=0
        n=len(nums)
        start=end=0
        preLen=0
        postLen=0
        while(end<n):
            num=nums[end]
            
            if num==1:
                preLen+=1
                end+=1
                
            else:
                start=end+1
                end+=1
                while(end<n and nums[end]!=0):
                    end+=1
                    postLen+=1
               
                maxLen=max(maxLen,preLen+postLen)
                
                preLen=postLen
                postLen=0
                
            maxLen=max(maxLen,preLen+postLen-1)

        return maxLen


        
