class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=end=0

        n=len(nums)

        while(end<n):
            num=nums[end]

            if num==0: k-=1

            if k<0:
                if nums[start]==0:
                    k+=1
                start+=1
            end+=1

        return end-start