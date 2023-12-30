# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, head: Optional[ListNode]) -> int:
        cur = head
        n=0
        while(cur!=None):
            n+=1
            cur=cur.next
        return n
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        n=self.get_len(head)
        if n==1: return None

        mid=n//2
        print(n,mid)
        cur = head
        i=0
        while(i<mid-1):
            cur=cur.next
            i+=1
        
        cur.next=cur.next.next
    
        return head
        