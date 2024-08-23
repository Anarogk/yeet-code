# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, s1 = l1, ""
        head2, s2 = l2, ""
        while head1:
            s1+=str(head1.val)
            head1 =head1.next
        while head2:
            s2+=str(head2.val)
            head2 = head2.next
        res = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        head = ListNode(0)
        temp = head
        for i in res:
            head.next = ListNode(i)
            head = head.next
        return temp.next