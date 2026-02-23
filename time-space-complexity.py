"""
====================================================
TIME COMPLEXITY & SPACE COMPLEXITY
====================================================

This file explains:

1. Time Complexity
2. Space Complexity

These concepts are used to measure algorithm efficiency.
They are expressed using Big-O notation.
"""


# ====================================================
# TIME COMPLEXITY
# ====================================================

"""
Time Complexity Definition:
---------------------------
Time complexity measures how the running time of an
algorithm grows as the input size (n) increases.

It does NOT measure actual time in seconds.
It measures how the number of operations grows.

We express it using Big-O notation.
"""


# ---- Common Time Complexities ----

"""
O(1)  → Constant Time
O(log n) → Logarithmic Time
O(n)  → Linear Time
O(n log n) → Linearithmic Time
O(n²) → Quadratic Time
O(2ⁿ) → Exponential Time
"""


# ---- Examples ----

# O(1) - Constant Time
def get_first_element(arr):
    return arr[0]


# O(n) - Linear Time
def print_all_elements(arr):
    for item in arr:
        print(item)


# O(n²) - Quadratic Time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


"""
Explanation:

If input size doubles:

O(1)  → stays same
O(n)  → doubles
O(n²) → becomes 4 times larger
O(2ⁿ) → grows extremely fast
"""


# ====================================================
# SPACE COMPLEXITY
# ====================================================

"""
Space Complexity Definition:
----------------------------
Space complexity measures how much extra memory
an algorithm uses as input size increases.

This includes:
- Variables
- Data structures
- Function call stack (recursion)
"""


# ---- Examples ----

# O(1) - Constant Space
def sum_two_numbers(a, b):
    result = a + b
    return result


# O(n) - Linear Space
def copy_array(arr):
    new_arr = []
    for item in arr:
        new_arr.append(item)
    return new_arr


# O(n) - Recursive Space Example
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


"""
Explanation:

Recursive factorial uses O(n) space
because each function call waits on the stack.

Iterative factorial would use O(1) space.
"""


# ====================================================
# TIME VS SPACE TRADEOFF
# ====================================================

"""
Sometimes we use more memory to make code faster.

Example:
- Using a dictionary (hash map) speeds up lookups (O(1))
- But it consumes extra memory (O(n))

This is called a Time-Space Tradeoff.
"""


# ====================================================
# SUMMARY
# ====================================================

"""
Time Complexity → How fast an algorithm grows.
Space Complexity → How much memory it consumes.

Good algorithms aim for:
- Low time complexity
- Low space complexity

In interviews:
Most common focus:
O(1), O(log n), O(n), O(n log n), O(n²)
"""