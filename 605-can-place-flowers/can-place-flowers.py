class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start,end=0,1
        res=0
        lfb=len(flowerbed)
        
        if lfb==1 and flowerbed[0]==0: return True

        while(end<lfb):
     
            if sum(flowerbed[start:end+1])==0: 
                res+=1
                start=end
            else: start+=1
            
            end=start+2
        
        if start+2==lfb:
            if sum(flowerbed[start:])==0: res+=1
     

        return res>=n


