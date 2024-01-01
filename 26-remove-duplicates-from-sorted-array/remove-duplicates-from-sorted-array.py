class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i,scanner=1,0

        # if n<2: return n

        while(i<n and scanner<n):
            num=nums[scanner] 
            scanner+=1
            while(scanner<n and num==nums[scanner]):
                scanner+=1
            
            print(num,scanner,i)

            if scanner<n:
                nums[i]=nums[scanner]
                i+=1
                

            
        return i


        