"""
Problem: Palindrome Check
Return True if a string reads the same forwards and backwards.

Approach: Two-pointer technique - one pointer starts at the front,
one at the back, moving toward each other, comparing characters at
each step. Stops early on the first mismatch.

Time Complexity: O(n) - each character checked at most once
Space Complexity: O(1) - only two integer pointers used, no copies
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("madam"))  # True
    print(is_palindrome("hello"))  # False