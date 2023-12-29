class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        presum=0
        temp=0
        for alt in gain:
            temp+=alt
            presum=max(temp,presum)
        
        return presum

        