class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]

    def insert_string(self, string):

        if len(string):
            if self.children[ord(string[0]) - 97] == None:
                self.children[ord(string[0]) - 97] = TrieNode()

            self.children[ord(string[0]) - 97].insert_string(string[1:])


class Trie:
    def __init__(self, string):
        self.root = TrieNode()

        for i in range(len(string)):
            self.root.insert_string(string[i:])

    def count_distinct_substrings(self, node=None):
        count = 0
        if not node:
            node = self.root

        for child in node.children:
            if child:
                # print("yes")
                count += self.count_distinct_substrings(child) + 1

        return count

trie = Trie("ababa")

print(trie.count_distinct_substrings())
