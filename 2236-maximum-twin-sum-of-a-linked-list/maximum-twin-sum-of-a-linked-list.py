# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head: Optional[ListNode])-> Optional[ListNode]:
        prev=None
        cur=head
        while(cur!=None):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        return prev


    def pairSum(self, head: Optional[ListNode]) -> int:

        slow,fast=head,head.next
        
        # traverse to mid
        while fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        mid=slow.next

        # reverse mid to tail
        head2=self.reverse(mid)

        # compute sums
        max_sum=0
        cur1,cur2=head,head2
        while(cur2!=None):
            max_sum=max(max_sum,(cur1.val+cur2.val))
            cur1=cur1.next
            cur2=cur2.next
        
        return max_sum



      
        