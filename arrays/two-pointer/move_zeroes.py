"""
Problem: Move Zeroes
Move all zeroes in an array to the end while maintaining the relative
order of the nonzero elements, in place.

Approach: Two-pointer, read/write style. "i" scans through every
element. "j" marks the next open slot for a nonzero value. Whenever
a nonzero is found, swap it into position j and advance both pointers;
zeroes are simply skipped over by i alone.

Time Complexity: O(n) - single pass
Space Complexity: O(1) - in-place swaps only
"""

def move_zeroes(nums):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            i += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # expected: [1, 3, 12, 0, 0]