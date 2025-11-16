class Solution:
    @staticmethod
    def format(interval)-> str:
        a,b=interval
        return f"{a}->{b}" if a!=b else str(a)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]

        if len(nums)==0: return []
        if len(nums)==1: return [str(nums[0])]
        interval = [nums[0],nums[0]+1]

        for num in nums[1:]:
            a,b=interval
            if num in range(a,b+1):
                interval[1]+=1
            else :
                interval[1]-=1
                ranges.append(Solution.format(interval))
                interval[0]=num
                interval[1]=num+1

        interval[1]-=1
        ranges.append(Solution.format(interval))

        return ranges


        







# [0,2,3,4,6,8,9]
# 0,0
# 2,4
# 6,6
# 8,9

# [0,2->4,6,8->9]