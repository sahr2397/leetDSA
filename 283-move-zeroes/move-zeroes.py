class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index=0
        for i in range(len(nums)):
            if nums[i]!=0 and nums[zero_index]==0:
                nums[zero_index],nums[i]=nums[i],nums[zero_index]
            if nums[zero_index]!=0:
                zero_index+=1