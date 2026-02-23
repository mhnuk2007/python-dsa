"""
EXTRACT DIGITS FROM A NUMBER

This file demonstrates two approaches to extract
digits from a number and analyzes their complexity.
"""


# ====================================================
# VERSION 1: USING STRING CONVERSION
# ====================================================
def extract_digits(n):
    for i in range(len(str(n))):
        print(n % 10)
        n = n // 10

"""
🔎 What Happens Internally:

str(n) → converts number to string
len(str(n)) → counts digits
Loop runs once per digit

Each iteration:
    % 10 → O(1)
    // 10 → O(1)

Let:
d = number of digits in n

Since:
d ≈ log10(n)

⏱ Time Complexity:
str(n) → O(d)
Loop runs d times → O(d)
Total: O(d) + O(d) = O(d)

Since d = log n:
✅ Time Complexity = O(log n)

💾 Space Complexity:
str(n) creates a string of length d
❌ Space Complexity = O(log n)
"""


# ====================================================
# VERSION 2: OPTIMIZED (NO STRING CONVERSION)
# ====================================================
def extract_digits_optimized(n):
    while n > 0:
        print(n % 10)
        n = n // 10

"""
🔎 What Happens:

Loop runs until number becomes 0
Each iteration removes one digit
No string conversion

Again:
d = number of digits

⏱ Time Complexity:
Loop runs d times.
✅ Time Complexity = O(log n)

💾 Space Complexity:
No extra string created
Only few variables used
✅ Space Complexity = O(1)
"""


# ====================================================
# FINAL COMPARISON
# ====================================================
"""
🔥 Final Comparison:

| Version                  | Time     | Space    |
|--------------------------|----------|----------|
| Using str(n)             | O(log n) | O(log n) |
| Optimized (while loop)   | O(log n) | O(1)     |
"""


# ====================================================
# IMPORTANT CONCEPT
# ====================================================
"""
🧠 Important Concept:

Whenever you repeatedly:
- Divide by 10
- Divide by 2
- Remove digits
- Halve a number

You should think:
Time Complexity = O(log n)

Because the number shrinks exponentially.
"""


# ====================================================
# INTERVIEW TAKEAWAY
# ====================================================
"""
🎯 Interview Takeaway:

The optimized version is better because:
- Same time complexity
- Better space efficiency
- Cleaner logic
- No unnecessary string conversion
"""


# ====================================================
# TESTING
# ====================================================
n = 7865

print("Version 1 (using str):")
extract_digits(n)

print("\nVersion 2 (optimized):")
extract_digits_optimized(7865)




            