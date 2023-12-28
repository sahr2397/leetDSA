class Solution:
    def push(self,es: str, c:str):
        return [c]+es
    def decodeString(self, s: str) -> str:
        
        stack=[]
        for c in s:

            if c=="]":
                es=[]
                while stack[-1]!="[":
                   es = self.push(es,stack.pop())
                
                stack.pop()
                k=[]
                while stack and stack[-1].isdigit():
                    k=self.push(k,stack.pop())
                
                k=int("".join(k))
                es=es*k
                es="".join(es)
                stack.append(es)

            else:
                stack.append(c)

        return "".join(stack)


        