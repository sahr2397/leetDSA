class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        iList=[]
        word=list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowels.append(s[i])
                iList.append(i)
        j=len(vowels)-1
        for i in iList:
            word[i]=vowels[j]
            j-=1

        return "".join(word)
