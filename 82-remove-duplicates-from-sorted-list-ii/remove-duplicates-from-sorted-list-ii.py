# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        freq = Counter(arr)
        unique_vals = [x for x in arr if freq[x] == 1]
        unique_vals.sort()
        def array_to_linkedlist(unique_vals):
            if len(unique_vals) == 0:
                return None
            new_head = ListNode(unique_vals[0])
            current = new_head
            for i in range(1, len(unique_vals)):
                current.next = ListNode(unique_vals[i])
                current = current.next
            return new_head
        return array_to_linkedlist(unique_vals)