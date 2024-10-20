class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_of_val=0
        for i in range(len(nums)):
            if nums[i]==val: 
                count_of_val+=1
                nums[i]=2000

        nums.sort()
            
        return len(nums)-count_of_val
