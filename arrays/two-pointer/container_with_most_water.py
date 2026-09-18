"""
Problem: Container With Most Water
Given heights of vertical lines, find two lines that together with the
x-axis form a container holding the most water.

Approach: Two pointers starting at both ends. The container's height
is limited by the shorter line, so always move the pointer at the
shorter line inward - moving the taller one can only shrink the width
without any chance of increasing the height, so it can never improve
the answer.

Time Complexity: O(n) - single pass
Space Complexity: O(1)
"""

def max_area(height):
    i = 0
    j = len(height) - 1
    area = 0
    while i < j:
        h = min(height[i], height[j])
        width = j - i
        area = max(area, h * width)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return area


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected: 49