"""
Problem: Subarray Product Less Than K (LeetCode 713)
Given an array of positive integers and k, return the number of
contiguous subarrays whose product is strictly less than k.

Approach: Variable-size sliding window. Expand right and multiply the
running product by nums[right]. While the product is >= k, divide by
nums[left] and move left forward. Once the window is valid, every
subarray ending at right and starting between left and right is valid,
so add right - left + 1 to the count. If k <= 1, no product can be
below k (all numbers are >= 1), so return 0 immediately.

Time Complexity: O(n) - left and right each move forward at most n times
Space Complexity: O(1)
"""

def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0
    left = 0
    product = 1
    count = 0
    for right in range(len(nums)):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count


if __name__ == "__main__":
    print(num_subarray_product_less_than_k([10, 5, 2, 6], 100))  # expected: 8
    print(num_subarray_product_less_than_k([1, 2, 3], 0))        # expected: 0