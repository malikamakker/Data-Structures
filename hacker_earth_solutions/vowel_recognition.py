n = int(input())

for i in range(n):
    str = input()
    sum = 0
    substr_count_end = []
    substr_count_start = []
    substr_count_start.append(0)
    substr_count_end.append(0)
    vowel_pos = []
    for j in range(1, len(str)+1):
        substr_count_end.append(substr_count_end[j-1] + len(str) - j + 1)
        substr_count_start.append(substr_count_start[j-1] + j)
        if str[j-1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_pos.append(j)
    sum = 0
    for j in vowel_pos:
        sum = sum + len(str) - j + 1 + substr_count_end[j-1] - substr_count_start[j-1]
    print(sum)