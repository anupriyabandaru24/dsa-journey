"""
Problem: Average of a List
Return the average (mean) of a list of numbers, without using built-in
average/statistics functions.

Approach: Sum all numbers, divide by count. Handle the empty-list edge
case explicitly instead of letting it crash or silently returning 0.

Time Complexity: O(n) - sum() scans the list once
Space Complexity: O(1) - no extra storage needed
"""

def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot compute average of an empty list")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(average([10, 20, 30]))  # 20.0
    print(average([5]))           # 5.0