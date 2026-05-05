# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or k==0:
            return head
        curr=head
        count=0
        while curr:
            count=count+1
            curr=curr.next 
        k=k%count
        for i in range(k):
            curr=head
            for j in range(count-2):
                curr=curr.next
            curr1=head
            head=curr.next
            curr.next.next=curr1
            curr.next=None
        return head       