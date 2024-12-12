class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0: return []
        ranges=[]
        
        r=[nums[0],nums[0]]
        for num in nums[1:]:
            if r[1]+1==num:
                r[1]=num
            else:
                if r[0]==r[1]: ranges.append(str(r[0]))
                else : ranges.append(str(r[0])+"->"+str(r[1]))
                r=[num,num]
        if r[0]==r[1]: ranges.append(str(r[0]))
        else : ranges.append(str(r[0])+"->"+str(r[1]))

        return ranges


        