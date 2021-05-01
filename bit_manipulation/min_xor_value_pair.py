class node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

class binary_tree:

    def __init__(self):
        self.root = node()

    def insert(self, num):

        temp = self.root

        for i in range(31, -1, -1):
            bit = (num>>i) & 1
            # print(bit),
            if bit:
                if not temp.right:
                    temp.right = node()
                temp = temp.right
            else:
                if not temp.left:
                    temp.left = node()
                temp = temp.left

        temp.value = num
        # print(temp.value)

    def min_xor(self, num):

        temp = self.root
        # print(num)
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # print(bit),
            if bit:
                if temp.right:
                    # print(1),
                    temp = temp.right
                else:
                    # print(i),
                    temp = temp.left
            else:
                if temp.left:
                    # print(0),
                    temp = temp.left
                else:
                    # print(i),
                    temp = temp.right
        print(temp.value),
        print(num)
        return num^temp.value


bt = binary_tree()
str = "1 2 3 4 5"
arr = list(map(int, str.split(" ")))

bt.insert(arr[0])

min_val = 1000

for i in range(1, len(arr)):
    min_val = min(min_val, bt.min_xor(arr[i]))

    bt.insert(arr[i])

print(min_val)
