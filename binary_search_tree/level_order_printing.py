class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

class bst:
    def __init__(self, root):
        self.root = root

    def determine_height(self, node=self.root):
        if node:
            h = 1 + max(
                self.determine_height(node.left),
                self.determine_height(node.right)
            )
        else:
            return 0
        return h

    def print_level(self, h, l=0, node=self.root):
        if l==h:
            print(f"{node.num} ", end="")
            return
        elif l<h:
            self.print_level(h, l+1, node.left)
            self.print_level(h, l+1, node.right)

    def print_tree(self):
        h = self.determine_height()
        for i in range(h):
            self.print_level(i)
            print("")
