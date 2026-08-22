"""
Problem: Find the Largest Number
Find the largest number in a list without using max().

Approach: Track the largest value seen so far, starting at negative
infinity so any real number in the list will beat it immediately.

Time Complexity: O(n) - one pass, must check every number
Space Complexity: O(1)
"""

def find_largest(numbers):
    largest = float('-inf')
    for num in numbers:
        if num > largest:
            largest = num
    return largest


if __name__ == "__main__":
    print(find_largest([3, 7, 2, 9, 4]))  # 9
    print(find_largest([-5, -1, -10]))    # -1