def knapsack(wt, val, w, n):
    table = [0 for x in range(w+1)]

    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1]<=j:
                table[j] = max(
                    val[i-1]+table[j-wt[i-1]],
                    table[j]
                )

    return table[w]

val = [10, 30, 20]
wt = [5, 10, 15]
w = 100
n = len(val)

print(knapsack(wt, val, w, n))