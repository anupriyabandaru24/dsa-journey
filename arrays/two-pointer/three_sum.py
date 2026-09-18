"""
Problem: 3Sum
Given an array, find all unique triplets that sum to zero.

Approach: Sort the array first. Fix one number (outer loop), then use
two-pointer technique on the remaining subarray to find pairs summing
to the negative of the fixed number. Skip duplicate values at three
points (outer loop, left pointer, right pointer) to avoid duplicate
triplets in the result.

Time Complexity: O(n^2) - outer loop O(n) * two-pointer scan O(n)
Space Complexity: O(1) extra, not counting the output list
"""

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    # expected: [[-1, -1, 2], [-1, 0, 1]]
