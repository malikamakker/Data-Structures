class Node:
    def __init__(self, num):
        self.num = num
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def insert(self, num):
        node = Node(num)
        if self.head==None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.num)
            temp = temp.next

    def middle_of_list(self):
        count = 0
        mid = self.head
        head = self.head

        while head:
            if count%2:
                mid = mid.next
            head = head.next
            count += 1

        if mid:
            print("Mid of list "+str(mid.num))

ll = linkedlist()

for i in range(1,11):
    ll.insert(i)

ll.print_list()

ll.middle_of_list()
