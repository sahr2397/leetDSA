class Solution:
    def reverseWords(self, s: str) -> str:
        wordList=s.split(" ")
        result=[]
        for word in wordList[-1::-1]:
            if word:
                result.append(word.strip())
        
        return " ".join(result)