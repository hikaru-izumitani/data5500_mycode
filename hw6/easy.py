"""
ChatGPT
https://chatgpt.com/share/6ad3b261-4e30-83e8-99e2-b7c22ef2c366

Time Complexity Analysis (from ChatGPT):
-The time complexity is O(n) because the function iterates through 
every element in the input array exactly once. Each iteration performs 
a constant-time addition. 

Auxiliary Space Complexity (from ChatGPT)
-The auxiliary space complexity is O(1) because the algorithm uses 
only a fixed number of additional variables, regardless of the input 
size.
"""

def calc_sum(arr):
    """
    Calculate the sum of all integers in an array.

    Args:
        arr: A list of integers.

    Returns:
        The sum of all integers in the array.

    Time complexity: O(n)
    Auxiliary space complexity: O(1)
    """
    # O(1): Auxiliary space complexity
    total_sum = 0
    # O(n): Time complexity
    for i in arr:
        total_sum +=i
    return total_sum


lst = [-4, 2, 4, 3, 6, 9, 0, 2]
result = calc_sum(lst)
print(f"Array: {lst}")
print(f"Sum: {result}")