"""
Given information about N petrol pumps (say arr[]) that are present in a circular path. The information consists of the distance of the next petrol pump from the current one (in arr[i][1]) and the amount of petrol stored in that petrol pump (in arr[i][0]). Consider a truck with infinite capacity that consumes 1 unit of petrol to travel 1 unit distance. The task is to find the index of the first starting point such that the truck can visit all the petrol pumps and come back to that starting point.

Note: Return -1 if no such tour exists.

Examples:

Input: arr[] = {{4, 6}, {6, 5}, {7, 3}, {4, 5}}. 
Output: 1
Explanation: If started from 1st index then a circular tour can be covered.

Input: arr[] {{6, 4}, {3, 6}, {7, 3}}
Output: 2
"""

def get_starting_point(arr):
    start = 0
    curr_petrol = 0
    previous_deficit = 0
    index = 0

    for petrol, distance in arr:
        curr_petrol += petrol - distance
        index += 1
        if curr_petrol < 0:
            start = index
            previous_deficit += curr_petrol
            curr_petrol = 0

    return start if curr_petrol + previous_deficit >= 0 else -1

assert (result := get_starting_point([[4, 6], [6, 5], [7, 3], [4, 5]])) == 1, result
assert (result := get_starting_point([[6, 4], [3, 6], [7, 3]])) == 2, result
