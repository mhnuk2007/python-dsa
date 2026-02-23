"""
====================================================
REVERSE AN ARRAY
====================================================

This file demonstrates different approaches to reverse an array
and analyzes their time and space complexity.

What is Array Reversal?
-----------------------
Reversing an array means changing the order of elements
so that the first element becomes last, second becomes
second-last, and so on.

Example:
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]

Key Concept:
- Swap elements from both ends
- Move toward the center
- Stop when pointers meet or cross
"""


# ====================================================
# VERSION 1: USING FOR LOOP
# ====================================================
def rev_arr_for_loop(arr):
    """
    Reverse array using for loop with index swapping.
    
    Algorithm:
    1. Loop from index 0 to middle of array
    2. Swap element at i with element at (n-1-i)
    3. Return the reversed array
    
    Visual for [1, 2, 3, 4, 5]:
    
    Index: 0 1 2 3 4
    Value: 1 2 3 4 5
    
    i=0: swap arr[0] and arr[4] → [5, 2, 3, 4, 1]
    i=1: swap arr[1] and arr[3] → [5, 4, 3, 2, 1]
    i=2: middle element, no swap needed
    
    Result: [5, 4, 3, 2, 1]
    
    Note: Modifies array IN-PLACE
    """
    n = len(arr)
    # Only need to swap first half with second half
    for i in range(n // 2):
        # Swap elements using Python tuple unpacking
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Loop runs n/2 times
   - Each swap is O(1)
   - Total: O(n/2) = O(n)

💾 Space Complexity: O(1)
   - In-place reversal
   - Only uses loop variable

✅ Efficient in-place reversal.
"""


# ====================================================
# VERSION 2: USING WHILE LOOP (TWO POINTERS)
# ====================================================
def rev_arr_while_loop(arr):
    """
    Reverse array using two pointer technique.
    
    Algorithm:
    1. Initialize start=0, end=len(arr)-1
    2. While start < end:
       - Swap elements at start and end
       - Move start forward, end backward
    3. Return the reversed array
    
    Visual for [1, 2, 3, 4, 5]:
    
    Step 1: start=0, end=4
            swap arr[0] and arr[4] → [5, 2, 3, 4, 1]
            start=1, end=3
            
    Step 2: start=1, end=3
            swap arr[1] and arr[3] → [5, 4, 3, 2, 1]
            start=2, end=2
            
    Step 3: start >= end, stop
    
    Result: [5, 4, 3, 2, 1]
    
    Note: Modifies array IN-PLACE
    """
    start, end = 0, len(arr) - 1
    
    while start < end:
        # Swap elements at start and end pointers
        arr[start], arr[end] = arr[end], arr[start]
        # Move pointers toward center
        start += 1
        end -= 1
    
    return arr


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Each iteration moves both pointers
   - At most n/2 iterations

💾 Space Complexity: O(1)
   - In-place reversal
   - Only two pointer variables

✅ This is the TWO POINTER TECHNIQUE - very common in DSA!
"""


# ====================================================
# VERSION 3: USING PYTHONIC METHOD (list.reverse())
# ====================================================
def rev_arr_pythonic(arr):
    """
    Reverse array using built-in list.reverse() method.
    
    This is the most Pythonic way for in-place reversal.
    
    Note: Modifies array IN-PLACE
    Returns: None (the list is modified in place)
    """
    return arr.reverse()


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
💾 Space Complexity: O(1)
   - In-place reversal

⚠️ Note: arr.reverse() returns None, not the array!
   The array is modified in place.
   
Correct usage:
   arr = [1, 2, 3]
   arr.reverse()  # arr is now [3, 2, 1]
   # NOT: arr = arr.reverse()  # This would set arr to None!
"""


# ====================================================
# VERSION 4: USING SLICING
# ====================================================
def rev_arr_slicing(arr):
    """
    Reverse array using Python slicing.
    
    arr[::-1] creates a new reversed array.
    
    Syntax: arr[start:end:step]
    - start: omitted (default 0)
    - end: omitted (default len(arr))
    - step: -1 (go backward)
    
    Note: Creates a NEW array (NOT in-place)
    """
    return arr[::-1]


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Creates new array of size n
   - Copies all elements in reverse order

💾 Space Complexity: O(n)
   - Creates a new array
   - Original array unchanged

📝 When to use:
   - Need to preserve original array
   - Want concise, readable code
   - Memory is not a concern
"""


# ====================================================
# VERSION 5: USING RECURSION
# ====================================================
def rev_arr_recursion(arr, left, right):
    """
    Reverse array using recursion.
    
    Algorithm:
    1. Base case: if left >= right, stop
    2. Swap elements at left and right
    3. Recurse with left+1, right-1
    
    Args:
        arr: Array to reverse
        left: Left index (start from 0)
        right: Right index (start from len-1)
    
    Returns:
        Reversed array (modified in-place)
    
    Visual for [1, 2, 3, 4, 5]:
    
    rev_arr_recursion([1,2,3,4,5], 0, 4)
        │ swap arr[0] and arr[4] → [5,2,3,4,1]
        └── rev_arr_recursion([5,2,3,4,1], 1, 3)
                │ swap arr[1] and arr[3] → [5,4,3,2,1]
                └── rev_arr_recursion([5,4,3,2,1], 2, 2)
                        │ left >= right, stop
                        └── return [5,4,3,2,1]
                └── return [5,4,3,2,1]
        └── return [5,4,3,2,1]
    
    Result: [5, 4, 3, 2, 1]
    """
    # Base case: pointers crossed or met at center
    if left >= right:
        return arr
    
    # Swap elements at left and right
    arr[left], arr[right] = arr[right], arr[left]
    
    # Recursive case: move pointers toward center
    return rev_arr_recursion(arr, left + 1, right - 1)


"""
🔎 Analysis:

⏱ Time Complexity: O(n)
   - Each recursive call swaps one pair
   - At most n/2 recursive calls

💾 Space Complexity: O(n)
   - Each recursive call adds a frame to call stack
   - Maximum recursion depth = n/2
   - For large arrays, may cause stack overflow

⚠️ Recursion is elegant but uses stack space.
   For production, prefer iterative approaches.
"""


# ====================================================
# COMPARISON
# ====================================================
"""
🔥 Comparison:

| Approach     | Time   | Space  | In-Place | Notes                        |
|--------------|--------|--------|----------|------------------------------|
| For loop     | O(n)   | O(1)   | Yes      | Simple and efficient         |
| While loop   | O(n)   | O(1)   | Yes      | Two pointer technique        |
| reverse()    | O(n)   | O(1)   | Yes      | Most Pythonic (returns None) |
| Slicing      | O(n)   | O(n)   | No       | Creates new array            |
| Recursion    | O(n)   | O(n)   | Yes      | Stack overhead               |

✅ Best for production: while loop or reverse()
✅ Best for interviews: while loop (shows two pointer technique)
📝 Most concise: slicing (but uses extra space)
"""


# ====================================================
# IN-PLACE VS NEW ARRAY
# ====================================================
"""
🧠 In-Place vs New Array:

In-Place Reversal:
- Modifies original array
- O(1) extra space
- Methods: for loop, while loop, reverse(), recursion

New Array Creation:
- Preserves original array
- O(n) extra space
- Methods: slicing arr[::-1], reversed()

When to use In-Place:
- Memory is limited
- Don't need original array
- Modifying data is acceptable

When to use New Array:
- Need to preserve original
- Functional programming style
- Avoiding side effects
"""


# ====================================================
# SWAP TECHNIQUE IN PYTHON
# ====================================================
"""
💡 Python Swap Technique:

Traditional swap (other languages):
    temp = a
    a = b
    b = temp

Python tuple unpacking:
    a, b = b, a

This is:
- More concise
- More readable
- No temporary variable needed
- Works for any number of variables

Examples:
    x, y = y, x              # Swap two variables
    a, b, c = c, b, a        # Swap first and last
    arr[i], arr[j] = arr[j], arr[i]  # Swap array elements
"""


# ====================================================
# EDGE CASES
# ====================================================
"""
Edge Cases to Consider:

1. Empty array []:
   - Nothing to reverse
   - Return []

2. Single element [1]:
   - No swap needed
   - Return [1]

3. Two elements [1, 2]:
   - One swap
   - Return [2, 1]

4. Odd length [1, 2, 3]:
   - Middle element stays in place
   - Return [3, 2, 1]

5. Even length [1, 2, 3, 4]:
   - All elements are swapped
   - Return [4, 3, 2, 1]
"""


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Interview Takeaways:

1. Know all approaches:
   - Two pointer (while loop) is most common
   - Python slicing is most concise
   - Recursion shows understanding of call stack

2. Complexity analysis:
   - All are O(n) time
   - In-place is O(1) space
   - Slicing creates new array O(n) space

3. Two pointer technique:
   - Fundamental DSA pattern
   - Used in many array problems
   - Same pattern as palindrome check

4. In-place vs new array:
   - Know when to use each
   - Clarify requirements in interviews

5. Python-specific:
   - arr.reverse() modifies in place, returns None
   - arr[::-1] creates new reversed array
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ARRAY REVERSAL TESTS")
    print("=" * 50)
    
    # Test each approach with fresh copies of the array
    original = [1, 2, 5, 8, 3, 9, 4]
    
    # For loop (in-place)
    arr1 = original.copy()
    print(f"\nOriginal array: {original}")
    print(f"For loop:       {rev_arr_for_loop(arr1)}")
    
    # While loop (in-place)
    arr2 = original.copy()
    result = rev_arr_while_loop(arr2)
    print(f"While loop:     {result}")
    
    # Pythonic reverse() (in-place)
    arr3 = original.copy()
    rev_arr_pythonic(arr3)
    print(f"reverse():      {arr3}")
    
    # Slicing (creates new array)
    arr4 = original.copy()
    print(f"Slicing:        {rev_arr_slicing(arr4)}")
    print(f"Original preserved: {arr4}")  # Original unchanged
    
    # Recursion (in-place)
    arr5 = original.copy()
    print(f"Recursion:      {rev_arr_recursion(arr5, 0, len(arr5) - 1)}")
    
    # Edge cases
    print("\n" + "=" * 50)
    print("EDGE CASES")
    print("=" * 50)
    
    # Empty array
    empty = []
    print(f"\nEmpty array: {rev_arr_slicing(empty)}")
    
    # Single element
    single = [1]
    print(f"Single element: {rev_arr_slicing(single)}")
    
    # Two elements
    two = [1, 2]
    print(f"Two elements: {rev_arr_slicing(two)}")
    
    # Odd length
    odd = [1, 2, 3]
    print(f"Odd length: {rev_arr_slicing(odd)}")