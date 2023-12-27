class Solution:
    def removeStars(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ch == "*":
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)