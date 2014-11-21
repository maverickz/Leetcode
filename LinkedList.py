import random

class Node(object):
    
    def __init__(self, value = None):
        self._value = value
        self._next_node = None

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next_node(self):
        return self._next_node
    @next_node.setter
    def next_node(self, value):
        self._next_node = value

class LinkedList(object):
    
    def __init__(self, value = None):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head
    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail
    @tail.setter
    def tail(self, value):
        self._tail = value
    
    def is_empty(self):
        return self.head == None
    
    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def search(self, value):
        curr_node = None
        prev_node = None
        if self.head:
            curr_node = self.head
            while curr_node and curr_node.value != value:
                prev_node = curr_node
                curr_node = curr_node.next_node
        
        if curr_node and curr_node.value != value:
            curr_node = None
            prev_node = None
        return (prev_node, curr_node)

    def delete(self, value):
        prev_node, curr_node = self.search(value)
        if not prev_node and not curr_node:
            return
        elif not prev_node:
            self.head = curr_node.next_node
        elif prev_node and curr_node:
            prev_node.next_node = curr_node.next_node
        elif self.tail == curr_node:
            self.tail = prev_node
            self.tail.next_node = None
        
        del curr_node

    def display(self):
        curr_node = self.head
        while curr_node:
            print curr_node.value, '->',
            curr_node = curr_node.next_node
        print 'None'

    def display_rev(self, node):
        if not node:
            return
        else:
            self.display_rev(node.next_node)
            print node.value


if __name__ == '__main__':
    list_obj = LinkedList()
    head = tail = None
    for val in xrange(1,11):
        list_obj.append(val)

    list_obj.display()
    for _ in xrange(10):
        val = random.randint(1,10)
        list_obj.delete(val)
        print 'Deleted', val
        list_obj.display()
        list_obj.display_rev(list_obj.head)



        








