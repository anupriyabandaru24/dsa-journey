"""
Problem: Find Duplicates
Given a list of numbers, return the numbers that appear more than once.

Approach: Count occurrences of every number using a dictionary, then
filter for keys whose count is greater than 1.

Time Complexity: O(n) - two passes, each O(n), simplifies to O(n)
Space Complexity: O(n) - dictionary can hold up to n entries
"""

def find_duplicates(nums):
    count = {}
    duplicates = []
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for key in count:
        if count[key] != 1:
            duplicates.append(key)
    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))  # expected: [1, 2]