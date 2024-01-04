class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m,n=len(word1),len(word2)
        i,j=0,0
        res=[]

        while(i<m and j<n):
            res.append(word1[i])
            res.append(word2[j])

            i+=1
            j+=1

        if i>=m:
            return "".join(res) + word2[j:]
        elif j>=n:
            return "".join(res) + word1[i:]
        
        return "".join(res)




        