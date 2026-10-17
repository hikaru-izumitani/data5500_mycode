"""
Chat GPT
https://chatgpt.com/share/6ad3b528-9150-83e8-814f-2282c3ce643d
"""

def find_second_largest(arr):
    """
    Find the second-largest distinct integer in a list.

    The second-largest integer is the greatest value that is
    strictly smaller than the largest value in the list.

    Args:
        arr (list[int]): A list of integers.

    Returns:
        int | None: The second-largest distinct integer, or None
        if fewer than two distinct values exist.

    Time Complexity:
        O(n), where n is the number of elements in arr.

    Auxiliary Space Complexity:
        O(1).
    """
    # O(1) time: Check whether the input has enough elements.
    if len(arr) < 2:
        return None
    # O(1) auxiliary space: Store only two candidate values.
    largest = None
    secondLargest = None
    # O(n) time: Process each element exactly once.
    for i in arr:
        if (largest is None) or (i > largest):
            secondLargest = largest
            largest = i

        elif (secondLargest is None) or ((largest != i) and (secondLargest < i)):
            secondLargest = i

    return secondLargest

lst = [3,-1,4,1,5,9,2,6,9]
print(f"List: {lst}")

ans = find_second_largest(lst)
print(f"Second Largest: {ans}")