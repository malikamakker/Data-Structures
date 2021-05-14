def count_sort(arr, digit):
    freq = [0 for i in range(10)]

    for num in arr:
        freq[(num/digit)%10] += 1

    for i in range(1, len(freq)):
        freq[i] += freq[i-1]

    new = [0 for i in range(len(arr))]

    for num in reversed(arr):
        new[freq[(num/digit)%10]-1] = num
        freq[(num/digit)%10] -= 1
    return new

arr = [66, 33, 1030, 555, 2]

maxx = 0
maxx = max(arr, key=lambda x: len(str(x)))
maxx = len(str(maxx))

digit = 1
for i in range(maxx):
    new = count_sort(arr, digit)
    arr = new
    digit  = digit * 10
print(new)
