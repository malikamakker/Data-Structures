class Node:
    def __init__(self, num):
        self.next = None
        self.num = num

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.num)
            temp = temp.next

list = LinkedList()
list.head = Node(3)
list.head.next = Node(4)
list.head.next.next = Node(6)

list.print_list()