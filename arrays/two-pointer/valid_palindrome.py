"""
Problem: Valid Palindrome
Given a string, determine if it's a palindrome after converting all
uppercase letters to lowercase and removing all non-alphanumeric
characters.

Approach: Two-pointer technique. Move left and right pointers toward
each other. Skip over any non-alphanumeric characters without
comparing. When both pointers land on alphanumeric characters, compare
them case-insensitively.

Time Complexity: O(n) - single pass, pointers move at most n times total
Space Complexity: O(1) - no extra string created, unlike building a
cleaned copy first
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                       # False