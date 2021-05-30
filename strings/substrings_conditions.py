class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.max_len = 5
        self.min_len = 4
        self.unique = 3
        self.count = 0

    def insert_string(self, string, chars, length=0, unique=0, maxx=0):

        if len(string):
            if length<=self.max_len and unique<=self.unique:

                if self.children[ord(string[0]) - 97] == None:
                    self.children[ord(string[0]) - 97] = TrieNode()

                self.count += 1
                if length>=self.min_len:
                    maxx = max(maxx, self.count)

                if chars[ord(string[0]) - 97]==0:
                    chars[ord(string[0]) - 97] = 1
                    unique += 1

                maxx = self.children[ord(string[0]) - 97].insert_string(string[1:], chars, length + 1, unique, maxx)
        else:
            if length <= self.max_len and unique <= self.unique:
                self.count += 1

                if length >= self.min_len:
                    maxx = max(maxx, self.count)

        return maxx


class Trie:
    def __init__(self, string):
        self.root = TrieNode()
        chars = [0 for i in range(26)]
        self.maxx = 0
        for i in range(len(string)):
            self.maxx = max(self.maxx, self.root.insert_string(string[i:], chars, 0, 0, self.maxx))
            chars = [0 for i in range(26)]

trie = Trie("abcabcabc")
print(trie.maxx)
