class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i,scanner=1,0

        while(scanner<n):
            num=nums[scanner] 
            scanner+=1
            while(scanner<n and num==nums[scanner]):
                scanner+=1


            if scanner<n:
                nums[i]=nums[scanner]
                i+=1
                

            
        return i


        