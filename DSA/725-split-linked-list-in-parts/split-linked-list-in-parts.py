# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        
        while current:
            count += 1
            current = current.next
        
        quotient, remainder = divmod(count, k)
        result = []
        prev = None
        current = head
        
        for _ in range(k):
            part_head = current
            for _ in range(quotient + (remainder > 0) - 1):
                if current:
                    current = current.next
            if current:
                prev = current
                current = current.next
                prev.next = None
            result.append(part_head)
            remainder -= 1
        
        return result