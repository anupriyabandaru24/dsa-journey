"""
Problem: Sort Colors (Dutch National Flag)
Given an array with only 0s, 1s, and 2s, sort it in place in one pass.

Approach: Three pointers - low, mid, high. Partition the array as you
scan: 0s go before "low", 2s go after "high", 1s stay in the middle.
When a 2 is swapped into "mid", don't advance mid - the swapped-in
value hasn't been checked yet.

Time Complexity: O(n) - single pass
Space Complexity: O(1) - in-place swaps only
"""

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        else:
            mid += 1
    return nums


if __name__ == "__main__":
    print(sort_colors([2, 0, 2, 1, 1, 0]))  # expected: [0, 0, 1, 1, 2, 2]
