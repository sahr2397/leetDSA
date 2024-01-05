class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        [0,0,0,1,0,1,0,0,0]
        [1,0,1,0,1,1,1,0,1,0,1,0]
        '''
        
        start, end = 0, 1
        result = 0
        if len(flowerbed)==1 and flowerbed[0]==0: result=1

        while end < len(flowerbed):
            
            window = flowerbed[start:end+1]
            
            print(window)
            if sum(window) == 0: 
                result += 1
                start=end
            else: start+=1
                
            end = start + 2

       
        if (start+2==len(flowerbed)):
            window = flowerbed[start:]
            print(window)
            if sum(window) == 0: result += 1
        elif len(flowerbed)>1 and flowerbed[end-4]!=0:
            window = flowerbed[end-3:]
            print(window)
            if sum(window) == 0: result += 1
        


        # print(result)
        return result >= n
            
        