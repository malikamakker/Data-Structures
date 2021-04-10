class Node:
    def __init__(self, num):
        self.next = None
        self.num = num

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp
    
    def insert_last(self, node):
        temp = self.head
        while(temp):
            last = temp
            temp = temp.next
        last.next = node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.num)
            temp = temp.next

linked_list = LinkedList()
linked_list.head = Node(1)
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(3)

linked_list.insert_head(Node(0))
linked_list.insert_last(Node(5))

linked_list.print_list()
