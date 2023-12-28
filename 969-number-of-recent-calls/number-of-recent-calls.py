class RecentCounter:

    def __init__(self):
        self.requests=[]
        
    # def push(self,t: int):
    #     self.requests=[t]+self.requests

    def out(self,i):
        self.requests=self.requests[i:]

    def ping(self, t: int) -> int:
        # self.push(t)
        self.requests.append(t)
        # prune
        i=0
        # print(t-3000,t)
        while(self.requests[i]<t-3000):
            i+=1

        if i>0:
            self.out(i)
        # print(self.requests)
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)