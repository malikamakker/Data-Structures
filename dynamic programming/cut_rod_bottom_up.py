
def cut_rod(price,max_len):
    table = [0 for x in range(max_len+1)]

    for i in range(1,max_len+1):
        max_val = 0
        for j in range(1,i):
            max_val = max(
                max_val,
                price[j-1] + table[i-j]
            )
        table[i] = max(
            max_val,
            price[i-1]
        )
    return table[max_len]

price = [3   ,5,   8,   9,  10,  17,  17,  20]
max_len = len(price)

print(cut_rod(price, max_len))
