class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Q=deque()
        for s in senate: Q.append(s)
        T=deque()

        while(True):
            senator = Q.popleft()

            while(Q and senator==Q[0]):
                T.append(Q.popleft())
           
            if Q:
                Q.popleft()
                Q.append(senator)
                Q.extendleft(T)
                T.clear()
            else:
                return "Radiant" if senator=="R" else "Dire"


            

            
