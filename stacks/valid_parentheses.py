"""
Problem: Valid Parentheses
Given a string of brackets, determine if every opening bracket has a
matching, correctly-ordered closing bracket.

Approach: Use a stack. Push opening brackets. On a closing bracket,
check the stack isn't empty and that the top matches the expected
opening bracket (via a dictionary mapping closing -> opening).

Time Complexity: O(n) - one pass, each bracket pushed/popped once
Space Complexity: O(n) - worst case, stack holds all characters
"""

def is_valid(s):
    brackets = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in "([{":
            brackets.append(i)
        elif i in pairs:
            if len(brackets) == 0:
                return False
            if brackets.pop() != pairs[i]:
                return False
    return len(brackets) == 0


if __name__ == "__main__":
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))      # False
    print(is_valid("([)]"))    # False
    print(is_valid("{[]}"))    # True