class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(s.split(" ")).lower().strip()
        s = "".join(list(c for c in s if c.isalnum()))
    
        if s[::-1]==s:
            return True
        else :
            return False
        