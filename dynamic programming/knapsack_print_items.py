def knapsack(wt, val, w, n):
    table = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] <= j:
                table[i][j] = max(
                    val[i-1] + table[i-1][j-wt[i-1]],
                    table[i-1][j]
                )
            else:
                table[i][j] = table[i-1][j]
    cap = w
    print(table[n][w])
    for i in range(n,0,-1):
        if table[i-1][cap] != table[i][cap]:
            items.append(wt[i-1])
            cap = cap - wt[i-1]

val = [40, 100, 50, 60]
wt = [20, 10, 40, 30]
w = 60
n = len(wt)
items = []
knapsack(wt, val, w, n)
print(items)
