class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start,end=0,1
        res=0
        lfb=len(flowerbed)
        
        if lfb==1 and flowerbed[0]==0: res=1

        while(end<lfb):

            win= flowerbed[start:end+1]

            if sum(win)==0: 
                res+=1
                start=end
            else:
                start+=1
            
            end=start+2
        
        if start+2==lfb:
            win = flowerbed[start:]
            if sum(win)==0: res+=1
        elif lfb>1 and flowerbed[end-4]!=0:
            win= flowerbed[end-3:]
            if sum(win)==0: res+=1

        return res>=n


