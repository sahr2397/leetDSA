class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        start=0
        end=n-1

        max_vol=min(height[0],height[n-1])*(end-start)

        while(start<end):
            h1,h2=height[start],height[end]
            vol=min(h1,h2)*(end-start)
            max_vol=max(max_vol,vol)
            if(h1<h2):
                start+=1
            else:
                end-=1
        return max_vol

        
        