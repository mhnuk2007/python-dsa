"""
COUNT DIGITS IN A NUMBER

This file demonstrates three approaches to count
the number of digits in a number and analyzes
their time and space complexity.
"""

import math

n = 8837923

# ====================================================
# VERSION 1: USING STRING CONVERSION
# ====================================================
def count_digits_str(n):
    return len(str(n))

print("Using str():", count_digits_str(n))

"""
🔎 Analysis:

- Converts number to string
- Counts characters (digits)
- Let d = number of digits ≈ log10(n)

Time Complexity: O(log n)
Space Complexity: O(log n)
"""

# ====================================================
# VERSION 2: USING WHILE LOOP
# ====================================================
def count_digits_while(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print("Using while loop:", count_digits_while(n))

"""
🔎 Analysis:

- Repeatedly divides number by 10
- Counts iterations until n becomes 0
- d = number of digits ≈ log10(n)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

# ====================================================
# VERSION 3: USING LOG10
# ====================================================
def count_digits_log(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1

print("Using log10:", count_digits_log(n))

"""
🔎 Analysis:

- Uses logarithm property: digits = floor(log10(n)) + 1
- Direct mathematical computation

Time Complexity: O(1)
Space Complexity: O(1)
"""

# ====================================================
# COMPARISON
# ====================================================

"""
🔥 Final Comparison:

| Method               | Time       | Space     |
|---------------------|------------|-----------|
| str()                | O(log n)   | O(log n) |
| while loop           | O(log n)   | O(1)     |
| log10 formula        | O(1)       | O(1)     |
"""

# ====================================================
# INTERVIEW TAKEAWAY
# ====================================================

"""
🎯 Takeaway:

- String conversion: simple but uses extra space
- While loop: efficient in space, same time complexity
- Logarithm: fastest and most space-efficient
- Always consider input size and algorithm efficiency
"""