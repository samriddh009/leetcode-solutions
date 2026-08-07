class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        cur = self.head
        while cur and count<index:
            cur = cur.next
            count+=1
        if cur is None :
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next = self.head
        self.head = newnode

    def addAtTail(self, val: int) -> None:
        newnode = ListNode(val)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newnode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        count = 0
        cur = self.head
        while cur and count < index - 1:
            cur = cur.next
            count += 1
        if cur is None:
            return
        newnode = ListNode(val)
        newnode.next=cur.next
        cur.next = newnode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        cur = self.head
        while count<index-1 and cur:
            cur= cur.next
            count+=1
        if cur is None or cur.next is None:
            return
        cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)