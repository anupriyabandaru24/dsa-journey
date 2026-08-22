"""
Problem: Factorial (Recursion)
Return n! = n x (n-1) x (n-2) x ... x 1

Approach: Recursion - base case is n=0 or n=1 (returns 1 directly).
Recursive case multiplies n by factorial(n-1), moving toward the base case.

Time Complexity: O(n) - n recursive calls before hitting base case
Space Complexity: O(n) - each call sits on the call stack until unwound
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))  # 120
    print(factorial(0))  # 1