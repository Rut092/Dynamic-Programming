# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left==right:
            return head
        elif left==1:
            prev=None
            curr=head
            end_connection=head
            num=1
            while(num<=right):
                nxt_node=curr.next
                curr.next=prev
                prev=curr
                curr=nxt_node
                num+=1
            end_connection.next=curr
            return prev
                
        else:
            start_connection=None
            prev=None
            curr=head
            main=head
            end_connection=head
            num=1
            while(num!=left):
                start_connection=curr
                curr=curr.next
                end_connection=curr
                num+=1
            while(num<=right):
                nxt_node=curr.next
                curr.next=prev
                prev=curr
                curr=nxt_node
                num+=1
            end_connection.next=curr
            start_connection.next=prev
            return main