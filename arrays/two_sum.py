"""
Problem: Two Sum
Given a list of numbers and a target, return the indices of the two
numbers that add up to the target.

Approach: One-pass hash map. For each number, check if its complement
(target - number) has already been seen. If yes, return both indices.
If no, store the current number and its index for future lookups.

Time Complexity: O(n) - single pass through the list
Space Complexity: O(n) - dictionary can hold up to n entries
"""

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(two_sum([3, 2, 4], 6))       # expected: [1, 2]