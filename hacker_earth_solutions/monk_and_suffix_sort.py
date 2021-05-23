string, k = input().split(' ')
k = int(k)
n = len(string)

strings = []
for i in range(len(string)):
    strings.append(string[i:])
strings = sorted(strings)
print(strings[k-1])
