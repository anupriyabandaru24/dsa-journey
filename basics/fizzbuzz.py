"""
Problem: FizzBuzz
Print numbers 1 to n. Multiples of 3 -> "Fizz", multiples of 5 -> "Buzz",
multiples of both -> "FizzBuzz", otherwise print the number.

Approach: Check "divisible by both" first (most specific condition),
then fall back to single-condition checks. Order matters - checking
single conditions first would wrongly catch multiples of 15 as just
"Fizz" or "Buzz" and never reach the combined case.

Time Complexity: O(n) - one pass through 1..n
Space Complexity: O(1)
"""

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(15)