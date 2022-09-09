# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, firstHead: ListNode, secondHead: ListNode) -> Optional[ListNode]:
        
        count1=0
        count2=0
        temp1=firstHead
        temp2=secondHead

        while(temp1):
            temp1=temp1.next
            count1+=1
        while(temp2):
            temp2=temp2.next
            count2+=1

        if count1>count2:
            i=count1-count2
            while(i>0):
                firstHead=firstHead.next
                i-=1   
        else:
            i=count2-count1
            while(i>0):
                secondHead=secondHead.next
                i-=1

        while(firstHead and secondHead):
            if firstHead==secondHead:
                return firstHead

            firstHead=firstHead.next
            secondHead=secondHead.next

        return None