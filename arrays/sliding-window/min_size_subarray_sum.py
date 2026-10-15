"""
Problem: Minimum Size Subarray Sum (LeetCode 209)
Given an array of positive integers and a target, return the minimal
length of a contiguous subarray whose sum is >= target, or 0 if none.

Approach: Variable-size sliding window. Expand right and add nums[right]
to the running sum. While the sum is >= target, the window is valid, so
record its length, then shrink from the left (subtract nums[left], move
left forward) to look for a shorter valid window.

Time Complexity: O(n) - left and right each move forward at most n times
Space Complexity: O(1)
"""

def min_sub_array_len(target, nums):
    left = 0
    min_window = float('inf')
    sub_sum = 0
    for right in range(len(nums)):
        sub_sum += nums[right]
        while sub_sum >= target:
            min_window = min(min_window, right - left + 1)
            sub_sum -= nums[left]
            left += 1
    return min_window if min_window != float('inf') else 0


if __name__ == "__main__":
    print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))  # expected: 2
    print(min_sub_array_len(4, [1, 4, 4]))           # expected: 1
    print(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # expected: 0