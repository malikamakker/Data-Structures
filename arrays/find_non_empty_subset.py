"""
Given an array of N integers, the task is to find a non-empty subset such that the 
sum of elements of the subset is divisible by N. Output any such subset with its 
size and the indices(1-based indexing) of elements in the original array if it exists.

Input: arr[] = { 2, 3, 7, 1, 9 }
Output: 2
        1 2
The required subset is { 2, 3 } whose indices are 1 and 2.


Input: arr[] = {2, 11, 4}
Output: 2
        2 3 
"""

def find_subset(arr):
    n = len(arr)
    sum = 0
    prefix_map = {}
    for i in range(n):
        sum = (sum + arr[i]) % n
        if sum == 0:
            print(i+1)
            print(" ".join([str(j) for j in range(1, i+2)]))
            return
        elif sum in prefix_map:
            print(i - prefix_map[sum])
            print(" ".join([str(j) for j in range(prefix_map[sum]+2, i+2)]))
            return
        else:
            prefix_map[sum] = i
    
arr = [2, 3, 7, 1, 9]
find_subset(arr)

arr = [2, 11, 4]
find_subset(arr)
