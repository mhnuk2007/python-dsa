"""
====================================================
ARMSTRONG NUMBER
====================================================

This file demonstrates how to check if a number is
an Armstrong number and analyzes the complexity.

What is an Armstrong Number?
----------------------------
An Armstrong number (also called narcissistic number) is a number
that equals the sum of its digits each raised to the power of
the number of digits.

Examples:
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✅
- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✅
- 123 = 1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123 ❌
"""


# ====================================================
# VERSION 1: 3-DIGIT ARMSTRONG CHECK
# ====================================================
def is_armstrong_3digit(n):
    """
    Check if a 3-digit number is an Armstrong number.
    
    For 3-digit numbers: sum of cubes of digits
    Example: 153 = 1³ + 5³ + 3³
    """
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10        # Extract last digit
        sum += digit ** 3        # Add cube of digit to sum
        temp //= 10              # Remove last digit
    return sum == n


# ====================================================
# VERSION 2: 4-DIGIT ARMSTRONG CHECK
# ====================================================
def is_armstrong_4digit(num):
    """
    Check if a 4-digit number is an Armstrong number.
    
    For 4-digit numbers: sum of digits raised to power 4
    Example: 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
    """
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10        # Extract last digit
        sum += digit ** 4        # Add digit^4 to sum
        temp //= 10              # Remove last digit
    return sum == num


# ====================================================
# VERSION 3: 5-DIGIT ARMSTRONG CHECK
# ====================================================
def is_armstrong_5digit(num):
    """
    Check if a 5-digit number is an Armstrong number.
    
    For 5-digit numbers: sum of digits raised to power 5
    Example: 93084 = 9⁵ + 3⁵ + 0⁵ + 8⁵ + 4⁵
    """
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10        # Extract last digit
        sum += digit ** 5        # Add digit^5 to sum
        temp //= 10              # Remove last digit
    return sum == num


# ====================================================
# VERSION 4: GENERIC ARMSTRONG CHECK (ANY DIGITS)
# ====================================================
def is_armstrong(num):
    """
    Generic function to check Armstrong number for any digit count.
    
    Steps:
    1. Count the number of digits (d)
    2. Calculate sum of each digit raised to power d
    3. Compare sum with original number
    """
    # Count digits
    num_digits = len(str(num))
    
    # Calculate sum of digits raised to power num_digits
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10                # Extract last digit
        sum += digit ** num_digits       # Add digit^d to sum
        temp //= 10                      # Remove last digit
    
    return sum == num


# ====================================================
# COMPLEXITY ANALYSIS
# ====================================================
"""
🔎 Analysis:

Let d = number of digits in n

Since d ≈ log₁₀(n):

Loop runs d times (once per digit)

Each iteration:
- % 10 → O(1)
- ** power → O(1) for small digits
- //= 10 → O(1)

⏱ Time Complexity: O(d) = O(log n)
💾 Space Complexity: O(1) (only few variables)

For generic version:
- str(num) adds O(d) space
- But can be replaced with math to count digits
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Version              | Works For      | Time     | Space    |
|---------------------|----------------|----------|----------|
| 3-digit function    | 3 digits only  | O(log n) | O(1)     |
| 4-digit function    | 4 digits only  | O(log n) | O(1)     |
| 5-digit function    | 5 digits only  | O(log n) | O(1)     |
| Generic function    | Any digits     | O(log n) | O(log n)*|

* O(log n) space due to str() conversion for digit count
  Can be optimized to O(1) by counting digits mathematically
"""


# ====================================================
# OPTIMIZED GENERIC VERSION (O(1) SPACE)
# ====================================================
def is_armstrong_optimized(num):
    """
    Optimized generic function with O(1) space.
    Uses math to count digits instead of string conversion.
    """
    # Count digits using math (O(1) space)
    temp = num
    num_digits = 0
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    # Calculate sum of digits raised to power num_digits
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    
    return sum == num


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Takeaways:

- Armstrong number = sum of (digits ^ number_of_digits)
- Time complexity is always O(log n) because we process each digit
- Space complexity can be O(1) with math approach
- Generic function is more flexible than fixed-digit functions
- For competitive programming, prefer optimized O(1) space version
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    # Test 3-digit Armstrong numbers
    n = 153
    print(f"Is {n} a 3-digit Armstrong number? {is_armstrong_3digit(n)}")
    
    # Test 4-digit Armstrong numbers
    num4 = 9474
    print(f"Is {num4} a 4-digit Armstrong number? {is_armstrong_4digit(num4)}")
    
    # Test 5-digit Armstrong numbers
    num5 = 93084
    print(f"Is {num5} a 5-digit Armstrong number? {is_armstrong_5digit(num5)}")
    
    # Test generic function
    print(f"\nGeneric function tests:")
    print(f"Is 153 an Armstrong number? {is_armstrong(153)}")
    print(f"Is 9474 an Armstrong number? {is_armstrong(9474)}")
    print(f"Is 93084 an Armstrong number? {is_armstrong(93084)}")
    print(f"Is 123 an Armstrong number? {is_armstrong(123)}")
    
    # Test optimized function
    print(f"\nOptimized function tests:")
    print(f"Is 153 an Armstrong number? {is_armstrong_optimized(153)}")
    print(f"Is 9474 an Armstrong number? {is_armstrong_optimized(9474)}")