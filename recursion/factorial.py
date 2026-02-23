"""
====================================================
FACTORIAL OF A NUMBER
====================================================

This file demonstrates two approaches to calculate factorial:
1. Iterative (using loop)
2. Recursive

What is Factorial?
------------------
Factorial of n (written as n!) is the product of all positive
integers from 1 to n.

Formula: n! = n × (n-1) × (n-2) × ... × 2 × 1

Examples:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1 (by definition)
- 1! = 1

Factorial is used in:
- Permutations and Combinations
- Probability calculations
- Taylor series expansions
"""


# ====================================================
# VERSION 1: ITERATIVE APPROACH (USING LOOP)
# ====================================================
def fact_loop(n):
    """
    Calculate factorial using a loop.
    
    Algorithm:
    1. Start with result = 1
    2. Multiply result by each number from 1 to n
    3. Return the final result
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
🔎 Analysis:

Loop runs n times (from 1 to n).

Each iteration does one multiplication: O(1)

⏱ Time Complexity: O(n)
   - Loop runs n times
   - Each iteration is O(1)

💾 Space Complexity: O(1)
   - Only uses one variable (result)
   - Constant extra space

✅ Advantages:
   - No risk of stack overflow
   - Better space efficiency
   - Preferred for large n
"""


# ====================================================
# VERSION 2: RECURSIVE APPROACH
# ====================================================
def fact_rec(n):
    """
    Calculate factorial using recursion.
    
    Recursion breaks down the problem:
    n! = n × (n-1)!
    
    Base case: 0! = 1, 1! = 1
    Recursive case: n! = n × (n-1)!
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * fact_rec(n - 1)


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Function calls itself n times
   - Each call does O(1) work (multiplication)

💾 Space Complexity: O(n)
   - Each recursive call adds a frame to the call stack
   - Maximum depth = n
   - Stack grows linearly with n

⚠️ Risk: Stack Overflow
   - Python has a recursion limit (~1000 by default)
   - For n > ~1000, this will raise RecursionError
   - Use iterative approach for large n

Call Stack Visualization for fact_rec(5):

fact_rec(5) = 5 × fact_rec(4)
            = 5 × 4 × fact_rec(3)
            = 5 × 4 × 3 × fact_rec(2)
            = 5 × 4 × 3 × 2 × fact_rec(1)
            = 5 × 4 × 3 × 2 × 1
            = 120

Stack unwinds from bottom to top.
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Approach    | Time   | Space  | Stack Overflow Risk |
|-------------|--------|--------|---------------------|
| Iterative   | O(n)   | O(1)   | No                  |
| Recursive   | O(n)   | O(n)   | Yes (for large n)   |
"""


# ====================================================
# RECURSION ANATOMY
# ====================================================
"""
🧠 Understanding Recursion:

Every recursive function needs:

1. Base Case(s)
   - Condition that stops recursion
   - Without it: infinite recursion → stack overflow
   - Here: if n == 0 or n == 1, return 1

2. Recursive Case
   - Function calls itself with modified input
   - Must move toward base case
   - Here: return n * fact_rec(n - 1)

3. Progress Toward Base Case
   - Each call must get closer to base case
   - Here: n decreases by 1 each call
   - Eventually reaches n = 1

Flow Diagram:

fact_rec(4)
    │
    ├── returns 4 × fact_rec(3)
    │               │
    │               ├── returns 3 × fact_rec(2)
    │               │               │
    │               │               ├── returns 2 × fact_rec(1)
    │               │               │               │
    │               │               │               └── BASE CASE: returns 1
    │               │               │
    │               │               └── returns 2 × 1 = 2
    │               │
    │               └── returns 3 × 2 = 6
    │
    └── returns 4 × 6 = 24
"""


# ====================================================
# EDGE CASES
# ====================================================
"""
Edge Cases:

1. n = 0:
   - 0! = 1 (by mathematical definition)
   - Both functions return 1

2. n = 1:
   - 1! = 1
   - Both functions return 1

3. n < 0:
   - Factorial is undefined for negative numbers
   - Should handle with error or return None

4. Large n:
   - Iterative: works fine
   - Recursive: stack overflow error
   - Python default limit: ~1000 recursive calls
"""


# ====================================================
# HANDLING EDGE CASES
# ====================================================
def factorial_safe(n):
    """
    Factorial with input validation.
    
    Raises ValueError for negative numbers.
    Uses iterative approach for safety.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ====================================================
# TAIL RECURSION (Advanced)
# ====================================================
def fact_tail(n, accumulator=1):
    """
    Tail recursive factorial.
    
    In tail recursion, the recursive call is the last operation.
    This allows some languages to optimize (tail call optimization).
    
    Note: Python does NOT optimize tail recursion,
    so this still has O(n) space complexity.
    """
    if n == 0 or n == 1:
        return accumulator
    return fact_tail(n - 1, n * accumulator)


"""
Tail Recursion Explanation:

Regular recursion: return n * fact_rec(n - 1)
- Multiplication happens AFTER recursive call returns
- Need to keep n in stack frame

Tail recursion: return fact_tail(n - 1, n * accumulator)
- Recursive call is the LAST operation
- No work needed after call returns
- accumulator carries the running product

Languages like Scheme, Haskell optimize this to O(1) space.
Python does NOT, so it's still O(n) space.
"""


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Interview Takeaways:

1. Know both approaches
   - Iterative: O(n) time, O(1) space ✅
   - Recursive: O(n) time, O(n) space

2. Recursive structure:
   - Base case(s) - stops recursion
   - Recursive case - moves toward base case

3. Space complexity differs:
   - Iterative uses constant space
   - Recursive uses stack space

4. For production code:
   - Prefer iterative for large inputs
   - Use recursion for clarity on small inputs

5. Factorial grows very fast:
   - 10! = 3,628,800
   - 20! = 2.4 × 10¹⁸
   - 100! has 158 digits!
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    n = 10
    
    print("=" * 50)
    print("FACTORIAL COMPARISON")
    print("=" * 50)
    
    # Test both approaches
    print(f"\nFactorial of {n}:")
    print(f"  Iterative: {fact_loop(n)}")
    print(f"  Recursive: {fact_rec(n)}")
    print(f"  Tail recursive: {fact_tail(n)}")
    
    # Test edge cases
    print("\n" + "=" * 50)
    print("EDGE CASES")
    print("=" * 50)
    
    print(f"\n0! = {fact_loop(0)}")
    print(f"1! = {fact_loop(1)}")
    
    # Test safe version
    print("\n" + "=" * 50)
    print("SAFE VERSION")
    print("=" * 50)
    
    try:
        print(f"\n5! = {factorial_safe(5)}")
        print(f"(-5)! = {factorial_safe(-5)}")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Show factorial growth
    print("\n" + "=" * 50)
    print("FACTORIAL GROWTH")
    print("=" * 50)
    
    for i in [1, 5, 10, 15, 20]:
        print(f"{i}! = {fact_loop(i):,}")