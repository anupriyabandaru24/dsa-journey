"""
Problem: Max Consecutive Ones III (LeetCode 1004)
Given a binary array nums and an integer k, return the length of the
longest subarray containing only 1s if you may flip at most k zeros.

Approach: Variable-size sliding window. "Flip at most k zeros" is the same
as "find the longest window containing at most k zeros". Expand right one
step at a time and count zeros in the window. While the count exceeds k,
move left forward, and if the number left just passed was a 0, decrease
the count. After the window is valid, update the best length.

Time Complexity: O(n) - right and left each move forward at most n times
Space Complexity: O(1) - only a few integer variables
"""

def longest_ones(nums, k):
    left = 0
    max_len = 0
    count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            count += 1
        while count > k:
            left += 1
            if nums[left - 1] == 0:
                count -= 1
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # expected: 6
    print(longest_ones([1, 1, 0, 0, 1, 1, 1], 1))              # expected: 4