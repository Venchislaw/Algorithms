class SinglyListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"Node({self.val} | next={self.next})"


class DoublyListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"""Node({self.val} | prev={self.prev.val if self.prev
                else self.prev} | next={self.next.val if self.next else self.next})"""

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        
    def insert(self, val, strategy="head") -> None:
        if strategy == "head":
            node = SinglyListNode(val)
            node.next = self.head
            self.head = node
            if not self.head.next:
                self.tail = self.head
        elif strategy == "tail":
            node = SinglyListNode(val)
            if not self.head:
                self.head = node
                self.tail = node
            self.tail.next = node
            self.tail = node

    def remove(self, val):
        cur = self.head
        if cur.val == val:
            self.head = cur.next
            cur.next = None
            return self

        while cur.next and cur.next.val != val:
            cur = cur.next
        if cur.next:
            if cur.next is self.tail:
                self.tail = cur
            if not cur.next:
                return self
            cur.next = cur.next.next
        return self
    
    def __repr__(self) -> str:
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return ", ".join(res)

            
class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def insert(self, val, strategy="head"):
        if strategy == "head":
            if self.head:
                node = DoublyListNode(val, prev=None, next=self.head)
                self.head.prev = node
                self.head = node
            else:
                self.head = DoublyListNode(val, prev=None, next=self.head)
                self.tail = self.head
        
        elif strategy == "tail":
            if self.tail:
                node = DoublyListNode(val, prev=self.tail)
                self.tail.next = node
                self.tail = node
            else:
                node = DoublyListNode(val)
                self.head = node
                self.tail = node

    def remove(self, val):
        cur = self.head
        while cur and cur.val != val:
            cur = cur.next
        
        if cur:
            if cur is self.head:
                cur.next.prev = None
                self.head = cur.next
            if cur.next:
                cur.next.prev = cur.prev
            if cur.prev:
                cur.prev.next = cur.next
            if not cur.next:
                self.tail = cur.prev
        return self


    def __repr__(self) -> str:
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        
        return ", ".join(res)

list_ = DoublyLinkedList()
list_.insert(1, strategy="tail")
list_.insert(2, strategy="tail")
list_.insert(3, strategy="tail")
list_.remove(3)
print(list_)
print(list_.head, list_.tail)
