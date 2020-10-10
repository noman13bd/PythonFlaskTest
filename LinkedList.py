from Node import Node

class LinkedList:
    
    def __init__(self, head = None, tail = None, length = 0):
        self.head = head
        self.tail = tail
        self.length = length
        
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1
        
    def __str__(self):
        list_vals = []
        node = self.head
        while node:
            list_vals.append(node.data)
            node = node.next
            
        listToStr = ' '.join([str(elem) for elem in list_vals]) 
        return listToStr
    
    def print_vals(self):
        list_vals = []
        node = self.head
        while node:
            list_vals.append(node.data)
            node = node.next
            
        listToStr = 'values - ' + ' '.join([str(elem) for elem in list_vals]) 
        return listToStr
    
        