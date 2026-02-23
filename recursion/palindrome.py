"""
====================================================
STRING PALINDROME CHECK
====================================================

This file demonstrates different approaches to check if a
string is a palindrome and analyzes their complexity.

What is a Palindrome?
---------------------
A palindrome is a string that reads the same forward and backward.

Examples:
- "madam" → Palindrome ✅
- "racecar" → Palindrome ✅
- "hello" → Not a palindrome ❌
- "a" → Palindrome ✅ (single character)
- "" → Palindrome ✅ (empty string)

Palindrome check compares characters from both ends,
moving toward the center.
"""


# ====================================================
# VERSION 1: USING FOR LOOP
# ====================================================
def is_palindrome_for_loop(my_str):
    """
    Check if a string is palindrome using for loop.
    
    Algorithm:
    1. Loop from index 0 to middle of string
    2. Compare character at i with character at (len-1-i)
    3. If any pair doesn't match, return False
    4. If all pairs match, return True
    
    Visual for "madam":
    Index: 0 1 2 3 4
    Chars: m a d a m
    
    Compare: 
    - i=0: my_str[0]='m' vs my_str[4]='m' ✅
    - i=1: my_str[1]='a' vs my_str[3]='a' ✅
    - i=2: middle character, no need to compare
    
    Result: True
    """
    # Only need to check first half against second half
    for i in range(len(my_str) // 2):
        # Compare character from left with character from right
        if my_str[i] != my_str[len(my_str) - i - 1]:
            return False
    return True


"""
🔎 Analysis:

Loop runs n/2 times where n = length of string.

⏱ Time Complexity: O(n)
   - We check n/2 character pairs
   - Each comparison is O(1)
   - Total: O(n/2) = O(n)

💾 Space Complexity: O(1)
   - Only uses loop variable i
   - No extra data structures

✅ Efficient and straightforward approach.
"""


# ====================================================
# VERSION 2: USING WHILE LOOP (TWO POINTERS)
# ====================================================
def is_palindrome_while_loop(my_str):
    """
    Check if a string is palindrome using two pointers.
    
    Algorithm:
    1. Initialize start pointer at index 0, end pointer at last index
    2. While start < end:
       - Compare characters at start and end
       - If different, return False
       - Move pointers toward center
    3. Return True if all comparisons pass
    
    Visual for "racecar":
    
    Step 1: start=0, end=6
            'r' == 'r' ✅
            start=1, end=5
            
    Step 2: start=1, end=5
            'a' == 'a' ✅
            start=2, end=4
            
    Step 3: start=2, end=4
            'c' == 'c' ✅
            start=3, end=3
            
    Step 4: start >= end, stop
    Result: True
    """
    start = 0                    # Left pointer (start)
    end = len(my_str) - 1      # Right pointer (end)
    
    while start < end:
        # Compare characters at both pointers
        if my_str[start] != my_str[end]:
            return False
        # Move pointers toward center
        start += 1
        end -= 1

    
    return True


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Each iteration moves both pointers
   - At most n/2 iterations

💾 Space Complexity: O(1)
   - Only two pointer variables

✅ This is the TWO POINTER TECHNIQUE!
   - Very common in string/array problems
   - Efficient for pair comparisons
"""


# ====================================================
# VERSION 3: USING RECURSION
# ====================================================
def is_palindrome_rec(my_str, left, right):
    """
    Check if a string is palindrome using recursion.
    
    Algorithm:
    1. Base case: if left >= right, all pairs matched → True
    2. If characters at left and right differ → False
    3. Otherwise, recurse with moved pointers
    
    Recursive structure:
    - Base case: left >= right (crossed or met at center)
    - Recursive case: compare and recurse with smaller range
    
    Args:
        my_str: String to check
        left: Left index (start from 0)
        right: Right index (start from len-1)
    
    Returns:
        True if palindrome, False otherwise
    """
    # Base case: pointers crossed or met at center
    if left >= right:
        return True
    
    # If characters don't match, not a palindrome
    if my_str[left] != my_str[right]:
        return False
    
    # Recursive case: check inner substring
    return is_palindrome_rec(my_str, left + 1, right - 1)


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Each recursive call compares one pair
   - At most n/2 recursive calls

💾 Space Complexity: O(n)
   - Each recursive call adds a frame to call stack
   - Maximum recursion depth = n/2
   - For large strings, this can cause stack overflow

Call Stack Visualization for "madam":

is_palindrome_rec("madam", 0, 4)
    │ 'm' == 'm' ✅
    └── is_palindrome_rec("madam", 1, 3)
            │ 'a' == 'a' ✅
            └── is_palindrome_rec("madam", 2, 2)
                    │ left >= right
                    └── BASE CASE: return True
            └── return True
    └── return True

Result: True

⚠️ For long strings, recursion may cause stack overflow!
"""


# ====================================================
# VERSION 4: PYTHONIC WAY (STRING SLICING)
# ====================================================
def is_palindrome_pythonic(my_str):
    """
    Check palindrome using Python string slicing.
    
    my_str[::-1] reverses the string.
    Compare original with reversed.
    
    Most concise but creates a new string.
    """
    return my_str == my_str[::-1]


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Reversing string takes O(n)
   - Comparison takes O(n)
   - Total: O(n)

💾 Space Complexity: O(n)
   - Creates a reversed copy of the string
   - Uses O(n) extra space

📝 This is the most readable but least space-efficient.
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Approach     | Time   | Space  | Notes                        |
|--------------|--------|--------|------------------------------|
| For loop     | O(n)   | O(1)   | Simple and efficient         |
| While loop   | O(n)   | O(1)   | Two pointer technique        |
| Recursion    | O(n)   | O(n)   | Stack overhead, risk of TLE  |
| Pythonic     | O(n)   | O(n)   | Most readable, extra space   |

✅ Best for production: For loop or While loop (O(1) space)
✅ Best for interviews: While loop (shows two pointer technique)
📝 Most readable: Pythonic way (my_str == my_str[::-1])
"""


# ====================================================
# TWO POINTER TECHNIQUE EXPLAINED
# ====================================================
"""
🧠 Two Pointer Technique:

This is a fundamental technique in DSA:

1. Start with pointers at both ends
2. Move pointers toward each other
3. Compare/process elements at pointer positions

When to use:
- Palindrome checks
- Reversing arrays/strings
- Finding pairs with specific sum
- Container with most water
- Trapping rain water

Pattern:
    left = 0
    right = len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        left += 1
        right -= 1
"""


# ====================================================
# EDGE CASES
# ====================================================
"""
Edge Cases to Consider:

1. Empty string "":
   - Length = 0
   - Return True (empty is palindrome)

2. Single character "a":
   - Length = 1
   - Return True

3. Two characters "aa":
   - Compare index 0 with index 1
   - Return True if same

4. Two characters "ab":
   - Compare index 0 with index 1
   - Return False if different

5. Case sensitivity:
   - "Madam" vs "madam"
   - Usually case-insensitive in palindrome checks

6. Spaces and punctuation:
   - "A man, a plan, a canal: Panama"
   - Usually ignore non-alphanumeric characters
"""


# ====================================================
# EXTENDED VERSION: HANDLE EDGE CASES
# ====================================================
def is_palindrome_extended(my_str):
    """
    Handle case sensitivity and non-alphanumeric characters.
    
    Example:
    - "A man, a plan, a canal: Panama" → True
    - "Madam" → True
    """
    # Convert to lowercase and filter alphanumeric only
    cleaned = ''.join(char.lower() for char in my_str if char.isalnum())
    
    # Use two pointer approach
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Interview Takeaways:

1. Know all approaches:
   - Two pointer (while loop) is most common
   - Recursion shows understanding of call stack
   - Pythonic way shows language knowledge

2. Complexity analysis:
   - All are O(n) time
   - Iterative is O(1) space
   - Recursive and slicing are O(n) space

3. Two pointer technique:
   - Fundamental DSA pattern
   - Used in many string/array problems

4. Edge cases:
   - Empty string
   - Single character
   - Case sensitivity
   - Non-alphanumeric characters

5. Why not recursion in production:
   - Stack overhead
   - Risk of stack overflow for long strings
   - Python recursion limit ~1000
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "madam",
        "racecar",
        "hello",
        "a",
        "",
        "aa",
        "ab"
    ]
    
    print("=" * 50)
    print("STRING PALINDROME TESTS")
    print("=" * 50)
    
    for my_str in test_cases:
        print(f"\n'{my_str}':")
        print(f"  For loop:   {is_palindrome_for_loop(my_str)}")
        print(f"  While loop: {is_palindrome_while_loop(my_str)}")
        print(f"  Recursion:  {is_palindrome_rec(my_str, 0, len(my_str) - 1)}")
        print(f"  Pythonic:   {is_palindrome_pythonic(my_str)}")
    
    # Extended test
    print("\n" + "=" * 50)
    print("EXTENDED VERSION TESTS")
    print("=" * 50)
    
    extended_tests = [
        "A man, a plan, a canal: Panama",
        "Madam",
        "race a car"
    ]
    
    for test in extended_tests:
        print(f"\n'{test}':")
        print(f"  Extended: {is_palindrome_extended(test)}")