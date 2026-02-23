"""
====================================================
TIME LIMIT EXCEEDED (TLE)
====================================================

This file explains:

1. What is Time Limit Exceeded (TLE)
2. Why TLE happens
3. How Time Complexity relates to TLE
4. Examples of TLE and optimized solutions

TLE occurs when a program does not finish execution
within the allowed time limit.
"""


# ====================================================
# WHAT IS TIME LIMIT EXCEEDED (TLE)
# ====================================================
"""
Definition:
-----------
Time Limit Exceeded (TLE) happens when an algorithm
takes too long to execute for the given input size.

Most coding platforms impose strict time limits,
usually around 1–2 seconds.

If your algorithm performs too many operations,
it will exceed that limit.
"""


# ====================================================
# WHY TLE HAPPENS
# ====================================================
"""
TLE usually occurs because:

1. High time complexity (O(n²), O(2ⁿ), etc.)
2. Nested loops on large inputs
3. Repeated unnecessary computations
4. Inefficient data structures
5. Unoptimized recursion
"""

# ====================================================
# OPERATION LIMIT RULE
# ====================================================
"""
Rough Competitive Programming Rule:

10^8 operations ≈ 1 second

If input size is:

n ≤ 10^4  → O(n²) is acceptable
n ≤ 10^5  → O(n log n) or O(n)
n ≤ 10^6  → O(n)
n ≥ 10^7  → O(1) or O(log n)

If your algorithm exceeds this range → TLE
"""


# ====================================================
# EXAMPLE 1 — TLE CASE (O(n²))
# ====================================================
def find_duplicates(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


# ====================================================
# OPTIMIZED VERSION (O(n))
# ====================================================
def find_duplicates_optimized(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

"""
Time Complexity: O(n) ✅
Space Complexity: O(n)

Uses extra memory to avoid TLE.
"""


# ====================================================
# EXAMPLE 2 — RECURSION TLE (EXPONENTIAL)
# ====================================================
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

"""
Time Complexity: O(2^n) ❌
Space Complexity: O(n)

For n = 40 → Extremely slow → TLE
"""


# ====================================================
# OPTIMIZED FIBONACCI
# ====================================================
def fib_optimized(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

"""
Time Complexity: O(n) ✅
Space Complexity: O(1) ✅
"""


# ====================================================
# HOW TO FIX TLE
# ====================================================
"""
Strategies to avoid TLE:

1. Reduce Time Complexity
   - Replace O(n²) with O(n log n) or O(n)

2. Use Better Data Structures
   - Use set/dict instead of list for lookups

3. Avoid Repeated Computation
   - Use memoization (Dynamic Programming)

4. Use Prefix Sums / Sliding Window / Two Pointers
   - Optimize brute force approaches

5. Avoid Unnecessary Nested Loops
"""


# ====================================================
# TIME VS SPACE TRADEOFF
# ====================================================
"""
Sometimes we increase space to reduce time.

Example:
- Nested loops → O(n²), O(1)
- Using hash set → O(n), O(n)

More memory → Faster execution.
"""


# ====================================================
# SUMMARY
# ====================================================
"""
TLE = Your algorithm is too slow.

It is directly related to Time Complexity.

To avoid TLE:
- Analyze input constraints
- Choose correct algorithm
- Optimize nested loops
- Use efficient data structures

In interviews and competitive programming,
avoiding TLE is about choosing the right complexity.
"""

