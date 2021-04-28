# from ..binary_search_tree.level_order_printing import bst as printer
class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

class bst:
    def __init__(self, root):
        self.root = root

    def search(self, num):
        node = self.root
        while node:
            if node.num == num:
                return 1
            if node.num < num:
                node = node.right
            if node.num > num:
                node = node.left
        return 0

    def insert(self, num):
        node = self.root
        if node:
            while node:
                if node.num <= num:
                    if not node.right:
                        node.right = Node(num)
                        break
                    node = node.right
                else:
                    if not node.left:
                        node.left = Node(num)
                        break
                    node = node.left
        else:
            self.root = Node(num)

    def determine_height(self, node=None):
        if node:
            h = 1 + max(
                self.determine_height(node.left),
                self.determine_height(node.right)
            )
        else:
            return 0
        return h

    def print_level(self, h, l=0, node=None):
        if not node:
            return
        if l==h:
            print(node.num)
            return
        elif l<h:
            self.print_level(h, l+1, node.left)
            self.print_level(h, l+1, node.right)

    def print_tree(self):
        h = self.determine_height(self.root)
        for i in range(h):
            self.print_level(i, node=self.root)
            print("")

tree = bst(Node(5))
tree.insert(3)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(7)

tree.print_tree()
