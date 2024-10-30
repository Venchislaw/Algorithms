from linked_list import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def enque(self, val):
        self.insert(val, strategy="tail")

    def deque(self):
        if not self.head:
            raise IndexError("Deque from an empty queue")

        val = self.head.val
        self.head = self.head.next
        
        if not self.head:
            self.tail = None
        
        return val
    
queue = Queue()
queue.enque(3)
queue.enque(2)
queue.enque(1)
print(queue)
print(queue.deque())
print(queue)