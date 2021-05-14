arr = [1,9,0,2,1,0,8,4]

maxx = max(arr)

freq = [0 for i in range(maxx+1)]

for num in arr:
    freq[num] += 1

for i in range(1, len(freq)):
    freq[i] += freq[i-1]

new = [0 for i in range(len(arr))]

for num in arr:
    new[freq[num]-1] = num
    freq[num] -= 1

print(new)
