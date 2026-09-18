"""
Problem: Trapping Rain Water
Given heights of bars, compute how much water can be trapped between
them after raining.

Approach: Two pointers from both ends, tracking left_max and right_max
seen so far. Whichever side currently has the smaller max "controls"
the water level there - if left_max < right_max, water trapped at the
left pointer is safely bounded by left_max alone, so we can resolve
that side without knowing the exact right_max.

Time Complexity: O(n) - single pass
Space Complexity: O(1) - no extra arrays needed
"""

def trap(height):
    left_max = 0
    right_max = 0
    total_water = 0
    left = 0
    right = len(height) - 1
    while left <= right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            total_water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total_water += right_max - height[right]
            right -= 1
    return total_water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6