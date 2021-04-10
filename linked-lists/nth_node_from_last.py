class node:
    def __init__(self, num):
        self.num = num
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def nth_node_from_last(self, n):
        main = self.head
        ref = self.head

        for i in range(n):
            ref = ref.next

        while(ref):
            main = main.next
            ref = ref.next

        print("nth node from last "+str(main.num))

    def insert(self, node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.head = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.num)
            temp = temp.next

ll = linkedlist()

for i in range(10):
    ll.insert(node(i))

ll.print_list()
ll.nth_node_from_last(0)



