# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = []
        x = head
        i = 1
        while x and x.next and x.next.next:
            if (x.val < x.next.val > x.next.next.val) or \
               (x.val > x.next.val < x.next.next.val):
                a.append(i)
            x = x.next
            i += 1
        if len(a) < 2:
            return [-1, -1]
        mn = float('inf')
        for i in range(1, len(a)):
            mn = min(mn, a[i] - a[i - 1])
        mx = a[-1] - a[0]
        return [mn, mx]