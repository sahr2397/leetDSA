class RecentCounter:

    def __init__(self):
        self.requests=[]
        

    def out(self,i):
        self.requests=self.requests[i:]

    def ping(self, t: int) -> int:
      
        self.requests.append(t)

        # prune
        i=0
        while(self.requests[i]<t-3000):
            i+=1
        if i>0:
            self.out(i)
      
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)