"""
Problem: Reverse a String
Reverse a string without using slicing or reversed().

Approach: Walk backwards through the string with an index, building
a list of characters (not a string) and joining at the end. Using a
list + join() avoids the O(n^2) cost of repeated string concatenation,
since strings are immutable in Python.

Time Complexity: O(n)
Space Complexity: O(n) - new list/string of the same length
"""

def reverse_string(s):
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)


if __name__ == "__main__":
    print(reverse_string("hello"))  # "olleh"