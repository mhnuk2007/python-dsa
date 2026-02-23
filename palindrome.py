"""
PALINDROME CHECK IN A NUMBER

This file demonstrates two approaches to check if a number
is a palindrome and analyzes their time and space complexity.
"""


# ====================================================
# VERSION 1: USING STRING CONVERSION
# ====================================================
def is_palindrome_str(n):
    s = str(n)
    return s == s[::-1]

"""
🔎 Analysis:

- Convert number to string
- Reverse string using slicing
- Compare reversed string with original

Let d = number of digits

⏱ Time Complexity: O(d) ≈ O(log n)
💾 Space Complexity: O(d) (for string)
"""


# ====================================================
# VERSION 2: USING MATH APPROACH
# ====================================================
def is_palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return rev == n

"""
🔎 Analysis:

- Extract digits using modulo and division
- Build reversed number
- Compare with original

Let d = number of digits

⏱ Time Complexity: O(d) ≈ O(log n)
💾 Space Complexity: O(1) (only few variables)
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Version           | Time Complexity | Space Complexity |
|------------------|-----------------|------------------|
| Math approach     | O(log n)        | O(1)             |
| String approach   | O(log n)        | O(log n)         |
"""


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Takeaways:

- Math approach is space-efficient (O(1))
- String approach is simpler and easy to implement
- For very large numbers, prefer math approach
- Both have same time complexity O(log n)
"""


# ====================================================
# TESTING
# ====================================================
n = 4567654

print("String approach:", is_palindrome_str(n))
print("Math approach:", is_palindrome(n))
