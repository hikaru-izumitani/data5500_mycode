"""
ChatGPT
https://chatgpt.com/share/6ad3a7dc-2024-83e8-acfb-a5c4cc6ce65e
Prompt 1: Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array. what does it mean? interger list -> interger matrix ?
Prompt 2: what is the definition of difference? should I use abs?
Time Complexity Analysis:
- The function iterates through the array of length n exactly once to find both the maximum and minimum values: O(n).
- Inside the loop, constant time O(1) comparisons and updates are performed.
- Therefore, the overall time complexity of this solution is O(n).
"""

def calc_max_diff(arr):
    """
    Calculates the maximum difference between any two numbers in an array of integers.
    
    Definition:
    - The maximum difference in a set of numbers is always the difference between 
      the absolute maximum value and the absolute minimum value in that array 
      (i.e., max(arr) - min(arr)). Therefore, absolute values (abs()) are not needed 
      if we subtract the minimum from the maximum.
    
    Parameters:
    arr (list of int): The input list of integers.
    
    Returns:
    int or None: The maximum difference, or None if the array has fewer than 2 elements.
    """
    if len(arr) < 2:
        return None
    # O(n)
    max_num = None
    min_num = None

    # O(n): Time complexity
    for i in arr:
        if max_num is None or i > max_num:
            max_num = i

        if min_num is None or i < min_num:
            min_num = i
    return max_num - min_num

lst = [-1, 2,5, 4, 3, 3, 5, 6, 10, 24, 21, -3, -4]
result = calc_max_diff(lst)
print(f"Array: {lst}")
print(f"Maximum Difference: {result}")