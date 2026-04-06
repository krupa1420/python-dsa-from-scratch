class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    # O(1) time and space
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    # get node at index
    # O(n) time, O(1) space
    def get(self, index):
        # edge case: -1 or < length
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # update value at index
    # O(n) time because of get(), O(1) space
    def setvalue(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # print all node values
    # O(n) time, O(1) space
    def printll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    # add node to the end
    # O(1) time and space
    def append(self, value):
        newnode = Node(value)
        # edge case: if ll is empty
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else: # when ll is filled
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        return True

    # add node to the beginning
    # O(1) time and space
    def prepend(self, value):
        newnode = Node(value)
        # edge case: if ll is empty
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else: # there are items already in ll
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        return True

    # add node at a specific index
    # O(n) time, O(1) space
    def insert(self, index, value):
        # edge case: -1 or > length
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newnode = Node(value)
        temp = self.get(index - 1)
        newnode.next = temp.next
        temp.next = newnode
        self.length += 1
        return True

    # remove last node
    # O(n) time because we traverse to find second last node
    def pop(self):
        # edge case: if ll is empty
        if self.tail is None:
            return None
        # edge case: if this node has 2 or more items
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # edge case: if no items
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # remove first node
    # O(1) time and space
    def popfirst(self):
        # edge case: if 0 item in ll
        if self.length == 0:
            return None
        # edge case: if more than 2 items
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # edge case: if no items
        if self.length == 0:
            self.tail = None
        return temp.value

    # remove node at index
    # O(n) time, O(1) space
    def remove(self, index):
        # edge case: -1 or < length
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

    # reverse the linked list
    # O(n) time, O(1) space
    def reverse(self):
        #switch head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # variables for reversing
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before #flip the arrow other way 
            #making sure no gap
            before = temp 
            temp = after


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