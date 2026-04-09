# Queue Class (using Linked List)
# Queue supports insertion at rear and removal from front (FIFO)

class Node:
    # O(1) time and space
    def __init__(self, value):
        self.value = value      # store data
        self.next = None        # pointer to next node


class Queue:
    # O(1) time and space
    def __init__(self, value):
        newnode = Node(value)
        self.first = newnode    # front of queue
        self.last = newnode     # rear of queue
        self.length = 1         # size of queue

    # add node to rear
    # O(1) time and space
    def enqueue(self, value):
        newnode = Node(value)
        if self.length == 0:        # edge case: empty queue
            self.first = newnode
            self.last = newnode
        else:
            self.last.next = newnode  # link new node at end
            self.last = newnode       # update rear
        self.length += 1

    # remove node from front
    # O(1) time and space
    def dequeue(self):
        if self.length == 0:        # edge case: empty queue
            return None

        temp = self.first
        if self.length == 1:        # only one element
            self.first = None
            self.last = None
        else:
            self.first = self.first.next  # move front forward
            temp.next = None              # detach node

        self.length -= 1
        return temp.value                # return removed value

    # check front value without removing
    # O(1) time and space
    def peek(self):
        if self.length == 0:
            return None
        return self.first.value

    # check if queue is empty
    # O(1) time and space
    def is_empty(self):
        return self.length == 0

    # print all queue values (front to rear)
    # O(n) time, O(1) space
    def printqueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


# Example usage
myqueue = Queue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)

print("Queue after enqueue 1, 2, 3, 4:")
myqueue.printqueue()

print(f"Dequeued element is {myqueue.dequeue()}")
print(f"Front element is {myqueue.peek()}")

print("Queue after dequeue:")
myqueue.printqueue()

print(f"Is empty: {myqueue.is_empty()}")

myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()

print(f"Is empty after removing all: {myqueue.is_empty()}")
print(f"Dequeue from empty queue: {myqueue.dequeue()}")