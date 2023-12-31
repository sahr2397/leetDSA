# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head==None or head.next==None or head.next.next==None: return head


        odd=head
        even_head=head.next
        even=even_head

        while(even!=None and even.next!=None):
            odd.next=even.next
            even.next=odd.next.next

            odd=odd.next
            even=even.next
           
        odd.next=even_head
        
        return head

      