def knapsack(wt,val,w,n):
    table = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, w+1):
            if wt[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(
                    val[i-1] + table[i-1][j-wt[i-1]],
                    table[i-1][j]
                )
    return table[n][w]

wt = [1, 2, 3]
val = [10, 15, 40]
n = len(val)
w = 6
print(knapsack(wt, val, w, n))