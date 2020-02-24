from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    # enqueue
    def enqueue(self, value):
        pass

    # dequeue
    def dequeue(self):
        pass


    def len(self):
        pass

if __name__ == '__main__':
        q = Queue()
        q.enqueue(100)
        q.enqueue(101)
        q.enqueue(105)
        print(f'dequeue should return 100: {q.dequeue()}') # => 100
        print(f'Len should return 2: {q.len()}') # => 2
        print(f'dequeue should return 101: {q.dequeue()}') # => 101
        print(f'Len should return 1: {q.len()}') # =>  1
        print(f'dequeue should return 105: {q.dequeue()}') # => 105
        print(f'Len should return 0: {q.len()}') # =>  0
        print(f'dequeue should return None: {q.dequeue()}') # => None
        print(f'Len should return 0: {q.len()}') # => 0