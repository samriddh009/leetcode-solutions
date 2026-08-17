# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def divide(lists, left, right):
            if left>right:
                return None
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = divide(lists, left, mid)
            l2 = divide(lists, mid + 1, right)
            return mergeTwoLists(l1, l2)
        return divide(lists, 0, len(lists) - 1)
def mergeTwoLists(list1, list2): 
    dummy = ListNode() 
    tail = dummy 
    current1 = list1 
    current2 = list2 
    while current1 and current2: 
        if current1.val <= current2.val: 
            tail.next = current1 
            current1 = current1.next 
        else: 
            tail.next = current2 
            current2 = current2.next 
        tail = tail.next 
    tail.next = current1 if current1 else current2
    return dummy.next