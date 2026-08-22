"""
Problem: Character Frequency Count
Given a string, count how many times each character appears.

Approach: Single pass through the string, using a dictionary's .get()
method to either start a count at 1 or increment an existing count.

Time Complexity: O(n) - one pass through the string
Space Complexity: O(k) - k = number of unique characters
"""

def char_frequency(s):
    counts = {}
    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


if __name__ == "__main__":
    print(char_frequency("hello"))  # expected: {'h':1,'e':1,'l':2,'o':1}