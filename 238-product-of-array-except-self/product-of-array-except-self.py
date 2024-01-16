from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prodList=[]
        prod= reduce(lambda a,b: a*b, nums)
        for i in range(len(nums)):
            n=nums[i]
            if n:
                prodList.append(prod//n)
            else :
               p=reduce(lambda x,y: x*y, nums[:i] if nums[:i] else [1] )*reduce(lambda x,y: x*y, nums[i+1:] if nums[i+1: ] else [1])

               prodList.append(p)

        return prodList