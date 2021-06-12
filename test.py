# input

words = [
    ["however", (1, 10)],
    ["nice", (3, 15)],
    ["like", (5, 8)]
]
# sorting on y coordinate
words = sorted(words, key= lambda x:x[1][1])

# compute error margin
error = [abs(words[i][1][1] - words[i-1][1][1]) for i in range(1, len(words)) ]

average_diff = sum(error)/len(error)

lines = [words[0]]

for i in range(1, len(words)):
    if abs(words[i][1][1] - words[i-1][1][1]) <average_diff:
        lines.append(words[i])
    else:
        lines.sort(key= lambda x:x[1][0])
        line = ""
        for word in lines:
            line = line + word[0] + " "
        print(line)
        lines = []
        lines.append(words[i])
line = ""
for word in lines:
    line = line + word[0] + " "
print(line)