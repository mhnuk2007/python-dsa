"""
====================================================
DIVISORS AND PRIME FACTORS
====================================================

This file demonstrates how to find:
1. All divisors of a number
2. Prime factors of a number

Both algorithms are optimized using the square root trick.
"""

import math


# ====================================================
# FIND ALL DIVISORS
# ====================================================
def find_divisors(n):
    """
    Find all divisors of a number n.
    
    Divisors come in pairs:
    If i divides n, then n/i also divides n.
    Example: n=12, i=3 → n/i=4
    Both 3 and 4 are divisors.
    
    We only need to check up to √n because:
    - If i > √n, then n/i < √n (already found)
    - So all divisors are found by checking up to √n
    """
    divisors = []
    
    # Only check up to square root
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:                  # i is a divisor
            divisors.append(i)          # Add i
            if i != n // i:             # Avoid duplicate for perfect squares
                divisors.append(n // i) # Add the pair n/i
    
    divisors.sort()  # Sort for readable output
    return divisors


"""
🔎 Analysis:

Loop runs from 1 to √n, so √n iterations.

⏱ Time Complexity: O(√n)
   - Finding divisors: O(√n)
   - Sorting: O(d log d) where d = number of divisors
   - Total: O(√n + d log d)

💾 Space Complexity: O(d) where d = number of divisors
   - At most O(√n) divisors for any number

Example:
n = 12
√12 ≈ 3.46, so we check i = 1, 2, 3
i=1: 12%1=0 → add 1 and 12
i=2: 12%2=0 → add 2 and 6
i=3: 12%3=0 → add 3 and 4
Divisors: [1, 2, 3, 4, 6, 12]
"""


# ====================================================
# FIND PRIME FACTORS
# ====================================================
def find_prime_factors(n):
    """
    Find all prime factors of a number n.
    
    Algorithm:
    1. Try dividing by 2, 3, 4, ... up to √n
    2. If n is divisible by i, keep dividing by i
       until it's no longer divisible
    3. After all divisions, if n > 1, it's a prime factor itself
    
    Key insight:
    - We only need to check up to √n
    - If no factor found up to √n, the number is prime
    """
    prime_factors = set()  # Use set to avoid duplicates
    
    # Try each potential factor from 2 to √n
    for i in range(2, int(math.sqrt(n)) + 1):
        # Keep dividing by i while it's a factor
        while n % i == 0:
            prime_factors.add(i)  # i is a prime factor
            n //= i               # Reduce n by dividing by i
    
    # If n > 1 after all divisions, it's a prime factor
    if n > 1:
        prime_factors.add(n)
    
    return prime_factors


"""
🔎 Analysis:

Outer loop runs from 2 to √n, so √n iterations.

The inner while loop divides n each time.
Each division reduces n.
The total number of divisions across the entire algorithm is at most O(log n)
(when repeatedly dividing by 2).

But these divisions do NOT happen for every i.

⏱ Time Complexity: O(√n)

Why it is NOT O(√n × log n):

Case 1: n is prime (e.g., 10⁹ + 7)
   - Loop runs √n times
   - Inner while never runs
   - Time = O(√n)

Case 2: n = 2^k
   - Outer loop mostly skipped quickly
   - Inner while runs log n times
   - Time = O(log n)

The algorithm never does √n iterations each doing log n work.
So multiplication does not apply.

More precisely: O(√n + log n)
Since √n dominates log n:
Final Time Complexity = O(√n)

💾 Space Complexity: O(log n)
   - Number of distinct prime factors is at most log₂(n)
   - Example: 2³¹ has only 1 prime factor
   - Example: 2×3×5×7×11×13 has 6 prime factors

Example walkthrough:
n = 60
√60 ≈ 7.75, so we check i = 2, 3, 4, 5, 6, 7

i=2: 60%2=0 → add 2, n=30
     30%2=0 → add 2, n=15
     15%2≠0 → stop inner loop
i=3: 15%3=0 → add 3, n=5
     5%3≠0 → stop inner loop
i=4: 5%4≠0 → skip
i=5: 5%5=0 → add 5, n=1
     1%5≠0 → stop inner loop
n=1, so we don't add anything else

Prime factors: {2, 3, 5}
60 = 2² × 3 × 5
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Function           | Purpose          | Time     | Space    |
|-------------------|------------------|----------|----------|
| find_divisors     | All divisors     | O(√n)    | O(√n)    |
| find_prime_factors| Prime factors    | O(√n)    | O(log n) |
"""


# ====================================================
# IMPORTANT CONCEPTS
# ====================================================
"""
🧠 Why Check Only Up to √n?

For divisors:
- If i divides n, then n/i also divides n
- One of them must be ≤ √n
- So all divisors are found by checking up to √n

For prime factors:
- If n has a prime factor > √n, it can only have one
- Because two factors > √n would multiply to > n
- After dividing by all small factors, remaining n (if > 1) is prime

This is why we check: if n > 1 after the loop.
"""


# ====================================================
# EDGE CASES
# ====================================================
"""
Edge Cases to Consider:

1. n = 1:
   - Divisors: [1]
   - Prime factors: {} (empty, 1 has no prime factors)

2. n is prime:
   - Divisors: [1, n]
   - Prime factors: {n}

3. n is a perfect square:
   - Example: n=16
   - Divisors: [1, 2, 4, 8, 16]
   - Note: 4 appears only once (√16 = 4)

4. n is a power of 2:
   - Example: n=32
   - Prime factors: {2}
"""


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Interview Takeaways:

1. Always use √n optimization for divisor/factor problems
   - Reduces O(n) to O(√n)

2. Divisors come in pairs (i, n/i)
   - Add both at once to save iterations

3. For prime factors, keep dividing by same factor
   - Handles repeated factors like 2³ in 40

4. After checking all factors up to √n
   - If n > 1, it's a prime factor itself

5. Use set for prime factors to avoid duplicates
   - Or use list if you want to count multiplicities
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    # Test divisors
    print("=" * 50)
    print("DIVISORS TEST")
    print("=" * 50)
    
    test_cases = [12, 13, 16, 1, 100]
    for n in test_cases:
        print(f"Divisors of {n}: {find_divisors(n)}")
    
    # Test prime factors
    print("\n" + "=" * 50)
    print("PRIME FACTORS TEST")
    print("=" * 50)
    
    test_cases = [12, 60, 13, 100, 1]
    for n in test_cases:
        print(f"Prime factors of {n}: {find_prime_factors(n)}")
    
    # Detailed walkthrough
    print("\n" + "=" * 50)
    print("DETAILED WALKTHROUGH")
    print("=" * 50)
    
    n = 60
    print(f"\nFor n = {n}:")
    print(f"Divisors: {find_divisors(n)}")
    print(f"Prime factors: {find_prime_factors(n)}")
    print(f"Prime factorization: 60 = 2² × 3 × 5")