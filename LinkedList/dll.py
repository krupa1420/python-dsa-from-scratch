# Doubly Linked List Class
class Node:
    # O(1) time and space
    def __init__(self, value):
        self.value = value      # store node value
        self.next = None        # pointer to next node
        self.prev = None        # pointer to previous node
        

class DoublyLinkedList:
    # O(1) time and space
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node    # first node
        self.tail = new_node    # last node
        self.length = 1         # total number of nodes

    # print all node values
    # O(n) time, O(1) space
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)   # print current node value
            temp = temp.next    # move to next node
        
    # add node to the end
    # O(1) time and space
    def append(self, value):
        new_node = Node(value)
        if self.head is None:   # edge case: empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # connect old tail to new node
            new_node.prev = self.tail   # connect new node back to old tail
            self.tail = new_node        # move tail to new node
        self.length += 1
        return True

    # remove last node
    # O(1) time and space
    def pop(self):
        if self.length == 0:    # edge case: empty list
            return None
        temp = self.tail        # store last node
        if self.length == 1:    # edge case: only one node
            self.head = None
            self.tail = None 
        else:
            self.tail = self.tail.prev  # move tail backward
            self.tail.next = None       # remove forward link
            temp.prev = None            # fully detach removed node
        self.length -= 1
        return temp

    # add node to the beginning
    # O(1) time and space
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:    # edge case: empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # point new node to old head
            self.head.prev = new_node   # point old head back to new node
            self.head = new_node        # move head to new node
        self.length += 1
        return True

    # remove first node
    # O(1) time and space
    def pop_first(self):
        if self.length == 0:    # edge case: empty list
            return None
        temp = self.head        # store first node
        if self.length == 1:    # edge case: only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next  # move head forward
            self.head.prev = None       # remove backward link
            temp.next = None            # fully detach removed node
        self.length -= 1
        return temp

    # get node at index
    # O(n) time, O(1) space
    def get(self, index):
        if index < 0 or index >= self.length:   # edge case: invalid index
            return None
        
        if index < self.length / 2:   # search from head if index is in first half
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:                         # search from tail if index is in second half
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        
    # update value at index
    # O(n) time because of get(), O(1) space
    def set_value(self, index, value):
        temp = self.get(index)    # find node first
        if temp:
            temp.value = value    # change value
            return True
        return False              # edge case: invalid index
    
    # add node at a specific index
    # O(n) time, O(1) space
    def insert(self, index, value):
        if index < 0 or index > self.length:   # edge case: invalid index
            return False
        if index == 0:                         # edge case: insert at beginning
            return self.prepend(value)
        if index == self.length:               # edge case: insert at end
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)   # node before new node
        after = before.next            # node after new node

        new_node.prev = before         # connect new node backward
        new_node.next = after          # connect new node forward
        before.next = new_node         # connect previous node to new node
        after.prev = new_node          # connect next node back to new node
        
        self.length += 1   
        return True  

    # remove node at index
    # O(n) time, O(1) space
    def remove(self, index):
        if index < 0 or index >= self.length:   # edge case: invalid index
            return None
        if index == 0:                          # edge case: remove first node
            return self.pop_first()
        if index == self.length - 1:            # edge case: remove last node
            return self.pop()

        temp = self.get(index)       # node to remove
        
        temp.next.prev = temp.prev   # connect next node to previous node
        temp.prev.next = temp.next   # connect previous node to next node
        temp.next = None             # remove temp forward link
        temp.prev = None             # remove temp backward link

        self.length -= 1
        return temp
  


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()