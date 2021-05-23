import math

for i in range(int(input())):
    bits = [0 for i in range(30)]
    line = list(input().split(' '))
    arr = list(map(int, input().split(' ')))
    k = int(line[1])

    # calculate the bits
    for num in arr:
        for j in range(30):
            if num & (2 ** j):
                bits[j] += 1
    sums = [bits[j] * (2 ** j) for j in range(30)]
    sums = sorted(sums, reverse=True)

    # calculate max ways
    j = 0
    ways = 1
    while j < len(sums) and k > 0:
        count = 0

        if sums[j] == 0:
            ways = -1
            break

        while (j < (len(sums) - 1) and (sums[j] == sums[j + 1])):
            count += 1
            j += 1

        count += 1

        if ((k - count) < 0):
            ways *= int(math.factorial(count) / (math.factorial(count - k) * math.factorial(k)))
            break
        k = k - count
        j = j + 1
    print(ways)
