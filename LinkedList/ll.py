# Singly Linked List Class
class Node:
    # O(1) time and space
    def __init__(self, value):
        self.value = value      # store data
        self.next = None        # pointer to next node

class Linkedlist:
    # O(1) time and space
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode     # first node
        self.tail = newnode     # last node
        self.length = 1         # size of list

    # get node at index
    # O(n) time, O(1) space
    def get(self, index):
        if index < 0 or index >= self.length:   # edge case: invalid index
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next   # move step by step
        return temp

    # update value at index
    # O(n) time because of get(), O(1) space
    def setvalue(self, index, value):
        temp = self.get(index)   # find node first
        if temp:
            temp.value = value   # update value
            return True
        return False             # edge case: invalid index
    
    # print all node values
    # O(n) time, O(1) space
    def printll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)    # print each node
            temp = temp.next


    # add node to the end
    # O(1) time and space
    def append(self, value):
        newnode = Node(value)
        if self.head is None:   # edge case: empty list
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode   # connect last node to new node
            self.tail = newnode        # move tail
        self.length += 1
        return True

    # add node to the beginning
    # O(1) time and space
    def prepend(self, value):
        newnode = Node(value)
        if self.head is None:   # edge case: empty list
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head   # point new node to current head
            self.head = newnode        # update head
        self.length += 1
        return True

    # add node at a specific index
    # O(n) time, O(1) space
    def insert(self, index, value):
        if index < 0 or index > self.length:   # edge case: invalid index
            return False
        if index == 0:                         # edge case: insert at start
            return self.prepend(value)
        if index == self.length:               # edge case: insert at end
            return self.append(value)

        newnode = Node(value)
        temp = self.get(index - 1)   # node before position
        newnode.next = temp.next     # link new node
        temp.next = newnode
        self.length += 1
        return True

    # remove last node
    # O(n) time, O(1) space
    def pop(self):
        if self.tail is None:   # edge case: empty list
            return None

        temp = self.head
        pre = self.head

        while temp.next:        # go to last node
            pre = temp
            temp = temp.next

        self.tail = pre         # update tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0:    # edge case: list becomes empty
            self.head = None
            self.tail = None

        return temp.value

    # remove first node
    # O(1) time and space
    def popfirst(self):
        if self.length == 0:    # edge case: empty list
            return None

        temp = self.head
        self.head = self.head.next   # move head forward
        temp.next = None             # detach node
        self.length -= 1

        if self.length == 0:         # edge case: list becomes empty
            self.tail = None

        return temp.value

    # remove node at index
    # O(n) time, O(1) space
    def remove(self, index):
        if index < 0 or index >= self.length:   # edge case: invalid index
            return None
        if index == 0:                          # edge case: remove first
            return self.popfirst()
        if index == self.length - 1:            # edge case: remove last
            return self.pop()

        prev = self.get(index - 1)   # node before target
        temp = prev.next

        prev.next = temp.next        # skip over node
        temp.next = None            # detach node
        self.length -= 1
        return temp.value

    # reverse the linked list
    # O(n) time, O(1) space
    def reverse(self):
        temp = self.head
        self.head = self.tail       # swap head and tail
        self.tail = temp

        before = None
        for _ in range(self.length):
            after = temp.next       # store next node
            temp.next = before      # reverse pointer
            before = temp           # move before forward
            temp = after            # move temp forward


myll = Linkedlist(9)
myll.append(10)
myll.append(11)
myll.append(12)
myll.printll()
print(f"Pop last element is {myll.pop()}")

myll.prepend(8)
myll.prepend(7)
myll.printll()
print(f"Pop first element is {myll.popfirst()}")
myll.printll()

print("Test index")
print(f"index {myll.get(3).value}")

print("Set index")
print(f"index {myll.setvalue(3, 111)}")
myll.printll()

print(f"index add 0 is 0 {myll.insert(0, 0)}")
myll.printll()

print(f"index add 2 is 2 {myll.insert(2, 2)}")
myll.printll()

print(f"index add 2 is removed {myll.remove(2)}")
myll.printll()

print("reverse ll")
myll.reverse()
myll.printll()