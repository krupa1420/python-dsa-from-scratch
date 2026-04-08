# Stack Class (using Linked List)
# Stack does not support insert or delete at arbitrary index: only top access (LIFO)
class Node:
    # O(1) time and space
    def __init__(self, value):
        self.value = value      # store data
        self.next = None        # pointer to next node

class Stack:
    # O(1) time and space
    def __init__(self, value):
        newnode = Node(value)
        self.top = newnode      # top of stack
        self.length = 1         # size of stack

    # add node to top
    # O(1) time and space
    def push(self, value):
        newnode = Node(value)
        if self.length == 0:        # edge case: empty stack
            self.top = newnode
        else:
            newnode.next = self.top  # point new node to current top
            self.top = newnode       # update top
        self.length += 1

    # remove node from top
    # O(1) time and space
    def pop(self):
        if self.length == 0:        # edge case: empty stack
            return None

        temp = self.top
        self.top = self.top.next    # move top down
        temp.next = None            # detach node
        self.length -= 1
        return temp.value           # return popped value

    # check top value without removing
    # O(1) time and space
    def peek(self):
        if self.length == 0:        # edge case: empty stack
            return None
        return self.top.value

    # check if stack is empty
    # O(1) time and space
    def is_empty(self):
        return self.length == 0

    # print all stack values (top to bottom)
    # O(n) time, O(1) space
    def printstack(self):
        temp = self.top
        while temp is not None:     # fixed: was temp.next, skipped last node
            print(temp.value)
            temp = temp.next


mystack = Stack(4)
mystack.push(5)
mystack.push(6)
mystack.push(7)
print("Stack after push 4, 5, 6, 7:")
mystack.printstack()

print(f"Pop top element is {mystack.pop()}")
print(f"Peek top element is {mystack.peek()}")

print("Stack after pop:")
mystack.printstack()

print(f"Is empty: {mystack.is_empty()}")

mystack.pop()
mystack.pop()
mystack.pop()
print(f"Is empty after popping all: {mystack.is_empty()}")
print(f"Pop from empty stack: {mystack.pop()}")