def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0

    if wt[n-1] <= w:
        if mem[n][w]!=-1:
            return mem[n][w]
        else:
            max_val = max(
                val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),
                knapsack(wt,val,w,n-1)
                )
            mem[n][w] = max_val
    else:
        mem[n][w] = knapsack(wt, val, w, n-1)
    return mem[n][w]

val = [10, 15, 40]
wt = [1, 2, 3]
w = 6
n= len(val)

mem = [[-1 for x in range(w+1)] for y in range(n+1)]

print(knapsack(wt,val,w,n))
