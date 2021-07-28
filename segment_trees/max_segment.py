import math
def construct_segment_tree(array, start, end, node, n):
    if start < n and end >= 0 and start == end:
        tree[node] = (array[start], start, end)

    elif start<n and end>=0 and start<=end:
        mid = int((start+end)/2)

        left = construct_segment_tree(array, start, mid, 2*node+1, n)
        right = construct_segment_tree(array, mid+1, end, 2*node+2, n)

        if not left:
            tree[node] = (max(right[0], array[mid]), start, end)
        elif not right:
            tree[node] = (max(left[0], array[mid]), start, end)
        else:
            tree[node] = (max(left[0], right[0], array[mid]), start, end)

    elif start<n and end<0:
        tree[node] = (array[start], start, end)

    elif start>=n and end>=0:
        tree[node] = (array[end], start, end)

    elif start>end:
        tree[node] = (array[start], start, end)

    return tree[node]


def find_segment(pos, node):
    if node <len(tree) and tree[node]:
        s = tree[node][1]
        e = tree[node][2]
        maxx = tree[node][0]
        num = array[pos]

        if maxx <= num:
            return tree[node]

        left = find_segment(pos, 2 * node + 1)
        right = find_segment(pos, 2 * node + 2)

        if left and right:
            if (left[2] + 1) == right[1]:
                return (left[0], left[1], right[2])
            elif pos < left[1] and pos < left[2]:
                return left
            elif pos > right[1] and pos > right[2]:
                return right
        if left:
            return left
        if right:
            return right
    return None

array = [10,2,3,2,12]
n = len(array)

height = math.log(n, 2)

if int(height) != height:
    height = int(height) + 1

leaves = 2**height

tree = [None for i in range(2*leaves)]

print(construct_segment_tree(array, 0, n-1, 0, n))

index = 0

for i in range(height+1):
    for j in range(2**i):
        print(tree[index]),
        index += 1
    print("")
print(find_segment(2, 0))
