"""
====================================================
FIBONACCI SERIES
====================================================

This file demonstrates different approaches to generate
Fibonacci numbers and analyzes their complexity.

What is Fibonacci?
------------------
Fibonacci is a sequence where each number is the sum
of the two preceding ones.

Formula: F(n) = F(n-1) + F(n-2)

Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Starting values:
- F(0) = 0
- F(1) = 1
- F(2) = F(1) + F(0) = 1
- F(3) = F(2) + F(1) = 2
- F(4) = F(3) + F(2) = 3
- ...

Fibonacci appears in:
- Nature (flower petals, pinecones)
- Golden ratio calculations
- Algorithm analysis
- Financial modeling
"""


# ====================================================
# VERSION 1: ITERATIVE - PRINT ALL TERMS
# ====================================================
def fib_loop(n):
    """
    Print all Fibonacci numbers from F(0) to F(n).
    
    Uses two variables that keep shifting:
    - a = current Fibonacci number
    - b = next Fibonacci number
    
    Each iteration:
    - Print current (a)
    - Shift: a becomes b, b becomes a+b
    """
    a, b = 0, 1
    for i in range(n + 1):
        print(i, ":", a)
        a, b = b, a + b


"""
🔎 Analysis:

Loop runs n+1 times.

Each iteration:
- Print: O(1)
- Assignment: O(1)

⏱ Time Complexity: O(n)
💾 Space Complexity: O(1)

Example walkthrough for n = 5:

i=0: print 0, then a=1, b=1
i=1: print 1, then a=1, b=2
i=2: print 1, then a=2, b=3
i=3: print 2, then a=3, b=5
i=4: print 3, then a=5, b=8
i=5: print 5

Output: 0, 1, 1, 2, 3, 5
"""


# ====================================================
# VERSION 2: ITERATIVE - RETURN NTH TERM
# ====================================================
def fib_loop_nth(n):
    """
    Return only the nth Fibonacci number.
    
    Most efficient approach for single Fibonacci value.
    
    Args:
        n: Index of Fibonacci number (0-indexed)
        
    Returns:
        The nth Fibonacci number
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Loop runs n times
   - Each iteration is O(1)

💾 Space Complexity: O(1)
   - Only two variables used
   - Constant space

✅ This is the BEST approach for Fibonacci!
   - Optimal time and space
   - No recursion overhead
   - No stack overflow risk
"""


# ====================================================
# VERSION 3: RECURSIVE (NAIVE)
# ====================================================
def fib_rec(n):
    """
    Calculate nth Fibonacci using naive recursion.
    
    Directly follows the mathematical definition:
    F(n) = F(n-1) + F(n-2)
    
    ⚠️ WARNING: This is very inefficient!
    Time complexity is exponential O(2^n)
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case
    return fib_rec(n - 1) + fib_rec(n - 2)


"""
🔎 Analysis:

⏱ Time Complexity: O(2^n) ❌
   - Each call spawns two more calls
   - Forms a binary tree of calls
   - Exponential growth!

💾 Space Complexity: O(n)
   - Maximum recursion depth is n
   - Stack grows linearly

⚠️ This is EXTREMELY SLOW for large n!

Why is it O(2^n)?

Call tree for fib_rec(5):

                    fib(5)
                   /      \
              fib(4)      fib(3)
             /    \       /    \
         fib(3)  fib(2) fib(2) fib(1)
         /   \   /   \   /   \
     fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
     /   \
  fib(1) fib(0)

Notice: Many calculations are repeated!
- fib(3) calculated 2 times
- fib(2) calculated 3 times
- fib(1) calculated 5 times

This is why it's so slow.

Performance comparison:
- n = 10: ~1,000 calls
- n = 20: ~1,000,000 calls
- n = 40: ~1,000,000,000 calls
- n = 50: Too slow to complete!
"""


# ====================================================
# VERSION 4: RECURSIVE WITH MEMOIZATION
# ====================================================
def fib_memo(n, memo=None):
    """
    Calculate nth Fibonacci using memoization.
    
    Memoization stores previously computed results
    to avoid redundant calculations.
    
    This converts O(2^n) to O(n)!
    """
    if memo is None:
        memo = {}
    
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Compute and store in memo
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


"""
🔎 Analysis:

⏱ Time Complexity: O(n) ✅
   - Each Fibonacci value computed only once
   - Subsequent lookups are O(1)

💾 Space Complexity: O(n)
   - Memo dictionary stores n values
   - Plus recursion stack of depth n

Memoization eliminates redundant calculations!

Call tree with memoization for fib_memo(5):

fib(5) → needs fib(4) and fib(3)
    │
    fib(4) → needs fib(3) and fib(2)
        │
        fib(3) → needs fib(2) and fib(1)
            │
            fib(2) → needs fib(1) and fib(0)
                │
                fib(1) = 1 (base case)
                fib(0) = 0 (base case)
                memo[2] = 1
            
            fib(1) = 1 (base case)
            memo[3] = memo[2] + 1 = 2
        
        fib(2) = memo[2] = 1 (looked up!)
        memo[4] = memo[3] + memo[2] = 3
    
    fib(3) = memo[3] = 2 (looked up!)
    memo[5] = memo[4] + memo[3] = 5

Each value computed exactly once!
"""


# ====================================================
# VERSION 5: USING DP (BOTTOM-UP)
# ====================================================
def fib_dp(n):
    """
    Calculate nth Fibonacci using dynamic programming.
    
    Bottom-up approach: build array from F(0) to F(n).
    Same complexity as iterative, but shows DP concept.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Create array to store all Fibonacci values
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
💾 Space Complexity: O(n)

Note: This uses O(n) space for the array.
The iterative version (fib_loop_nth) achieves O(1) space
by only keeping the last two values.
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Approach        | Time     | Space    | Notes                    |
|-----------------|----------|----------|--------------------------|
| Iterative       | O(n)     | O(1)     | ✅ Best overall           |
| Recursive       | O(2^n)   | O(n)     | ❌ Very slow, avoid       |
| Memoization     | O(n)     | O(n)     | ✅ Good for multiple calls|
| DP (bottom-up)  | O(n)     | O(n)     | Good for learning DP     |
"""


# ====================================================
# WHEN TO USE EACH APPROACH
# ====================================================
"""
🎯 When to Use Each:

1. Iterative (fib_loop_nth):
   - Single Fibonacci value needed
   - Best time and space
   - Production code

2. Recursive (fib_rec):
   - NEVER in production!
   - Only for teaching recursion concepts
   - Shows why naive recursion can be bad

3. Memoization (fib_memo):
   - Multiple Fibonacci values needed
   - Recursive style preferred
   - Good tradeoff of readability vs efficiency

4. DP (fib_dp):
   - Learning dynamic programming
   - Need all values from F(0) to F(n)
   - Foundation for more complex DP problems
"""


# ====================================================
# INTERVIEW TIPS
# ====================================================
"""
💡 Interview Tips:

1. Always start with iterative solution
   - O(n) time, O(1) space
   - Shows you understand efficiency

2. If asked for recursive, mention the problem:
   "Naive recursion is O(2^n), very inefficient.
    We can optimize it with memoization."

3. Know the formula:
   F(n) = F(n-1) + F(n-2)
   F(0) = 0, F(1) = 1

4. Common follow-up questions:
   - "Can you optimize space?" → Yes, O(1) iterative
   - "What if we need many Fibonacci values?" → Memoization
   - "Can you prove the time complexity?" → Draw recursion tree

5. Matrix exponentiation can achieve O(log n):
   - Advanced technique
   - Good to mention if you know it
"""


# ====================================================
# BONUS: MATRIX EXPONENTIATION (O(log n))
# ====================================================
"""
For interviews, you can mention that there's an even faster
method using matrix exponentiation:

[[F(n+1), F(n)  ]]   [[1, 1]]^n
[[F(n),   F(n-1)]] = [[1, 0]]

This gives O(log n) time complexity.

However, this is advanced and rarely needed in interviews.
The iterative O(n) solution is usually sufficient.
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    n = 15
    
    print("=" * 50)
    print("FIBONACCI COMPARISON")
    print("=" * 50)
    
    # Print all Fibonacci numbers
    print(f"\nFirst {n+1} Fibonacci numbers:")
    fib_loop(n)
    
    # Compare approaches
    print("\n" + "=" * 50)
    print("NTH TERM COMPARISON")
    print("=" * 50)
    
    print(f"\n{n}th Fibonacci number:")
    print(f"  Iterative:  {fib_loop_nth(n)}")
    print(f"  Recursive:  {fib_rec(n)}")
    print(f"  Memoization: {fib_memo(n)}")
    print(f"  DP:         {fib_dp(n)}")
    
    # Performance warning
    print("\n" + "=" * 50)
    print("PERFORMANCE WARNING")
    print("=" * 50)
    
    print("\nNaive recursive Fibonacci:")
    print("  n=10: fast")
    print("  n=20: noticeable delay")
    print("  n=40: takes several seconds")
    print("  n=50: may take minutes!")
    print("\nAlways use iterative or memoization for large n.")
    
    # Edge cases
    print("\n" + "=" * 50)
    print("EDGE CASES")
    print("=" * 50)
    
    for i in [0, 1, 2]:
        print(f"F({i}) = {fib_loop_nth(i)}")