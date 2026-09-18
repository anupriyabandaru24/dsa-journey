"""
Problem: Two Sum II - Input Array Is Sorted
Given a sorted array and a target, return the 1-indexed positions of
two numbers that add up to the target.

Approach: Two-pointer technique. Since the array is sorted, start one
pointer at the beginning and one at the end. If their sum is too small,
move the left pointer up; if too big, move the right pointer down.

Time Complexity: O(n) - single pass
Space Complexity: O(1) - no extra data structures needed
"""

def two_sum_sorted(numbers, target):
    i = 0
    j = len(numbers) - 1
    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i + 1, j + 1]
        elif total < target:
            i += 1
        else:
            j -= 1
    return []


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))  # expected: [1, 2]