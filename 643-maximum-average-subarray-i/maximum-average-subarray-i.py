class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        start=0
        end=0
        maxsum=float('-inf')
        csum=0
        i=0
        while(end<n):
            csum+=nums[end]
            i+=1
            end+=1
            
            if k==i:
                maxsum=max(maxsum,csum)
                print(maxsum)
                csum-=nums[start]
                start+=1
                i-=1

        return maxsum/k


                

            