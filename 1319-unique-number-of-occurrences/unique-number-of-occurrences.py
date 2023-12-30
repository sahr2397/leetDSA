from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts=defaultdict(int)
        hmap=defaultdict(list)
        
        for a in arr: counts[a]+=1
        
        for count in counts.values(): 
            hmap[count].append(a)

        for nums in hmap.values():
            if len(nums)>1: return False
        
        return True
        