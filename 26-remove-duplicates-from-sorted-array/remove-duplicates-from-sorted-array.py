class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        currentUnique=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==currentUnique:
                nums[i]=200
            else:  
                currentUnique=nums[i]
                k+=1
        
        nums.sort()

        return k