# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        temp=head
        if head==None:
            return None
        while(temp!=None):
            temp=temp.next
            length+=1
            
        rot=k%length
        
        if rot==0:
            return head
        else:
            temp=head
            temp_h=1
            while(temp_h<length-rot):
                temp=temp.next
                temp_h+=1
                
            prev=temp
            while(prev.next!=None):
                prev=prev.next
            
            prev.next=head
            head=temp.next
            temp.next=None
            
            return head
        
                
            
            
        
        