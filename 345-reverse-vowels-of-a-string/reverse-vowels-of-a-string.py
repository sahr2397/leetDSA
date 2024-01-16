class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        s=list(s)
        start,end=0,len(s)-1

        while(start<end):
            if s[start] in vowels and s[end] in vowels:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1

            if s[start] not in vowels:
                start+=1
            if s[end] not in vowels:
                end-=1

        return "".join(s)