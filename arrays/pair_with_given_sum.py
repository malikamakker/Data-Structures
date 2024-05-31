"""
Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

Examples: 

Input: arr[] = {0, -1, 2, -3, 1}, x= -2
Output: Yes
Explanation: If we calculate the sum of the output,1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}, x = 0
Output: No

"""

def pair_with_given_sum(arr, sum):
    previous_elements = set()
    for x in arr:
        if sum - x in previous_elements:
            return True
        previous_elements.add(x)
    return False

arr = [0, -1, 2, -3, 1]
sum = -2
if pair_with_given_sum(arr, sum):
    print("Yes")
else:
    print("No")

arr = [1, -2, 1, 0, 5]
sum = 0
if pair_with_given_sum(arr, sum):
    print("Yes")
else:
    print("No")
