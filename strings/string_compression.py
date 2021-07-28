class trie_node:
    def __init__(self, char):
        self.char = char
        self.index = []
        self.next = [None for i in range(26)]

class trie:
    def __init__(self, string):
        self.root = trie_node('')
        self.string = string
        self.compression = []
        self.construct_trie()
        self.compute_compression()

    def add_string(self, string, start_index):
        # print("i="),
        # print(start_index),
        print(string)
        initial_index = start_index
        node = self.root
        match = False
        last_match_index_list = []
        length_matched = 0

        start = self.root.next[ord(self.string[start_index]) - 97]
        if start:
            match = True
            first_match_index_list = start.index

        for c in string:
            index = ord(c) - 97
            if not node.next[index]:
                node.next[index] = trie_node(c)
                match = False
            if match and node.next[index].index[-1]<initial_index:
                print(c),
                print(node.next[index].index),
                length_matched += 1
                # if (node.next[index].index[-1] + 1) == initial_index:
                #     print(length_matched),
                last_match_index_list = node.next[index].index
                # print(last_match_index_list)
            node = node.next[index]
            node.index.append(start_index)
            start_index = start_index + 1

        if len(last_match_index_list):
            print("l="),
            print(length_matched),
            print(first_match_index_list),
            print(last_match_index_list)
            for i in first_match_index_list:
                if (i+length_matched-1)==last_match_index_list[-2]:
                    return i, last_match_index_list[-2]

        return -1, -1

    def construct_trie(self):
        for i in range(len(self.string)):
            start, last_match = self.add_string(self.string[i:], i)
            # print(start),
            # print(last_match)
            if last_match!=-1 and last_match+1 == i:
                # print(self.string[:last_match+1])
                self.compression.append((start, last_match))

    def compute_compression(self):
        lenn = 0
        index = 0
        if len(self.compression):
            last_pair = self.compression[0]
        for pair in self.compression:
            if pair[0] != (last_pair[1]+1):
                if pair[0] > index:
                    lenn += pair[0] - index
                    index = pair[0]
                if pair[1] >= index:
                    lenn += pair[1] - index + 1
                index = (pair[1] - pair[0] + 1) + pair[1] + 1
            elif index<=pair[1] or (pair[0] == (last_pair[1]+1) and index==pair[1]+1):
                index = (pair[1] - pair[0] + 1) + pair[1] + 1
            last_pair = pair
            # print(pair),
            # print(index),
            # print(lenn)
            if index>=len(self.string):
                break
        if index<len(self.string):
            lenn += len(self.string) - index
        self.length = lenn

compression = trie("aabaaaba")
print(compression.compression)
print(compression.length)
