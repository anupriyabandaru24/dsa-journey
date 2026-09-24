"""
Problem: Sort Array By Parity
Given an array, move all even integers before all odd integers.
Relative order within evens/odds doesn't need to be preserved.

Approach: Two-pointer, same-direction (like Move Zeroes). "right" scans
every element. "left" marks the next position where an even number
belongs. When an even number is found, swap it into position left.

Time Complexity: O(n) - single pass
Space Complexity: O(1) - in-place swaps only
"""

def sort_array_by_parity(nums):
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums


if __name__ == "__main__":
    print(sort_array_by_parity([3, 1, 2, 4]))  # example: [2, 4, 3, 1]