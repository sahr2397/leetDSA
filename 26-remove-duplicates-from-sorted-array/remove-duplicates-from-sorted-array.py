class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i,scanner=0,0
        
        while scanner<len(nums):
            if nums[i]!=nums[scanner]:
                i+=1
                nums[i]=nums[scanner]
            scanner+=1

        return i+1