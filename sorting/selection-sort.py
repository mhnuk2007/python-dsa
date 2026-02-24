"""
====================================================
SELECTION SORT
====================================================

This file demonstrates the Selection Sort algorithm with
detailed explanations and complexity analysis.

What is Selection Sort?
-----------------------
Selection Sort is a simple comparison-based sorting algorithm.

The idea is simple:
- Divide the array into two parts: sorted (left) and unsorted (right)
- Repeatedly find the minimum element from unsorted part
- Move it to the end of sorted part

How It Works:
-------------
1. Start with the entire array as "unsorted"
2. Find the minimum element in the unsorted portion
3. Swap it with the first element of unsorted portion
4. Move the boundary between sorted and unsorted one position right
5. Repeat until the entire array is sorted

Example:
--------
Initial:  [3, 7, 4, 8, 5, 2, 9, 6, 1]
          ↑
          Start here (sorted portion is empty)

Step 1: Find min in entire array = 1 at index 8
        Swap arr[0] with arr[8]
        [1, 7, 4, 8, 5, 2, 9, 6, 3]
         ↑
         Sorted: [1]

Step 2: Find min from index 1 to end = 2 at index 5
        Swap arr[1] with arr[5]
        [1, 2, 4, 8, 5, 7, 9, 6, 3]
            ↑
            Sorted: [1, 2]

Step 3: Find min from index 2 to end = 3 at index 8
        Swap arr[2] with arr[8]
        [1, 2, 3, 8, 5, 7, 9, 6, 4]
               ↑
               Sorted: [1, 2, 3]

... and so on until fully sorted.

Final:    [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# ====================================================
# SELECTION SORT IMPLEMENTATION
# ====================================================
def selection_sort(arr):
    """
    Sort an array using Selection Sort algorithm.
    
    Algorithm:
    1. Iterate through the array from index 0 to n-1
    2. For each position i, find the minimum in arr[i:n]
    3. Swap the minimum with element at position i
    4. Continue until all positions are sorted
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        The sorted array (modified in-place)
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Assume current position has the minimum
        min_idx = i
        
        # Find the actual minimum in unsorted portion [i+1, n-1]
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum with the first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# ====================================================
# DETAILED VERSION WITH VISUALIZATION
# ====================================================
def selection_sort_verbose(arr):
    """
    Selection Sort with step-by-step visualization.
    Useful for understanding how the algorithm works.
    """
    n = len(arr)
    print(f"Initial array: {arr}")
    print("-" * 40)
    
    for i in range(n):
        min_idx = i
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Show what we're doing
        print(f"Step {i + 1}: Find min from index {i} to {n-1}")
        print(f"  Min value = {arr[min_idx]} at index {min_idx}")
        
        # Swap if necessary
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  Swap index {i} and {min_idx}")
        else:
            print(f"  No swap needed (already in place)")
        
        # Show current state
        sorted_part = arr[:i+1]
        unsorted_part = arr[i+1:]
        print(f"  Sorted: {sorted_part}, Unsorted: {unsorted_part}")
        print()
    
    print("-" * 40)
    print(f"Final sorted array: {arr}")
    return arr


# ====================================================
# COMPLEXITY ANALYSIS
# ====================================================
"""
🔎 Time Complexity Analysis:

The algorithm uses two nested loops:

Outer loop: runs n times (i = 0 to n-1)
Inner loop: runs (n-1), (n-2), ..., 1 times

Total comparisons = (n-1) + (n-2) + ... + 1
                 = n(n-1)/2
                 = n²/2 - n/2
                 = O(n²)

⏱ Time Complexity: O(n²)
   - Best Case:    O(n²) - Even if sorted, still checks all
   - Average Case: O(n²)
   - Worst Case:   O(n²)

💾 Space Complexity: O(1)
   - In-place sorting (only uses a few variables)
   - No extra arrays needed

🔄 Number of Swaps: O(n)
   - At most n-1 swaps (one per iteration)
   - Fewer swaps than Bubble Sort!

📊 Comparison with Other O(n²) Sorts:

| Algorithm       | Time (Best) | Time (Avg) | Time (Worst) | Space | Swaps |
|-----------------|-------------|------------|--------------|-------|-------|
| Selection Sort  | O(n²)       | O(n²)      | O(n²)        | O(1)  | O(n)  |
| Bubble Sort     | O(n)        | O(n²)      | O(n²)        | O(1)  | O(n²) |
| Insertion Sort  | O(n)        | O(n²)      | O(n²)        | O(1)  | O(n²) |

Selection Sort has the advantage of MINIMUM SWAPS.
"""


# ====================================================
# WHEN TO USE SELECTION SORT
# ====================================================
"""
✅ When Selection Sort is Good:

1. Small datasets (n < 50)
   - Simple to implement
   - Low overhead

2. Memory is very limited
   - O(1) space complexity
   - Only needs one extra variable

3. When swaps are expensive
   - Makes at most n-1 swaps
   - Minimum write operations

4. When array is almost sorted
   - Still works the same way
   - But Insertion Sort would be better

❌ When Selection Sort is NOT Good:

1. Large datasets
   - O(n²) time complexity
   - Too slow for n > 1000

2. Nearly sorted arrays
   - Still does O(n²) comparisons
   - Can't take advantage of existing order

3. When stability is required
   - Selection Sort is NOT stable
   - Equal elements may change relative order
"""


# ====================================================
# STABILITY IN SORTING
# ====================================================
"""
🧠 What is a Stable Sort?

A sorting algorithm is stable if it preserves the relative
order of equal elements.

Example:
Input:  [(3, 'a'), (1, 'b'), (3, 'c'), (2, 'd')]
        Note: Two elements with value 3

Stable sort output:
[(1, 'b'), (2, 'd'), (3, 'a'), (3, 'c')]
                           ↑       ↑
                        (3,'a') comes before (3,'c') - preserved!

Unstable sort output (could be):
[(1, 'b'), (2, 'd'), (3, 'c'), (3, 'a')]
                           ↑       ↑
                        Order changed!

Selection Sort is NOT stable because:
- When we swap, we might skip over equal elements
- The swap operation doesn't preserve relative order

To make Selection Sort stable:
- Use insertion instead of swapping
- Shift elements to make room for minimum
"""


# ====================================================
# SELECTION SORT VS BUBBLE SORT
# ====================================================
"""
📊 Selection Sort vs Bubble Sort:

Selection Sort:
- Finds minimum, then swaps once per pass
- O(n) swaps total
- Better when writes are expensive

Bubble Sort:
- Swaps adjacent elements repeatedly
- O(n²) swaps in worst case
- Better for nearly sorted (can terminate early)

Both have:
- O(n²) time complexity
- O(1) space complexity
- Simple implementation

Selection Sort is generally faster than Bubble Sort
because of fewer swap operations.
"""


# ====================================================
# EDGE CASES
# ====================================================
"""
Edge Cases to Consider:

1. Empty array []:
   - No iterations needed
   - Return []

2. Single element [1]:
   - No swaps needed
   - Return [1]

3. Two elements [2, 1]:
   - One comparison, one swap
   - Return [1, 2]

4. Already sorted [1, 2, 3]:
   - Still O(n²) comparisons
   - No swaps needed (min is already in place)

5. Reverse sorted [3, 2, 1]:
   - O(n²) comparisons
   - Maximum swaps (n-1)

6. Duplicate elements [3, 1, 2, 1]:
   - Works fine
   - But not stable (relative order of 1's may change)
"""


# ====================================================
# TAKEAWAYS
# ====================================================
"""
🎯 Interview Takeaways:

1. Know the algorithm:
   - Find minimum in unsorted portion
   - Swap with first unsorted element
   - Repeat

2. Time complexity:
   - Always O(n²) regardless of input
   - No best-case optimization

3. Space complexity:
   - O(1) - in-place sorting

4. Key advantages:
   - Simple implementation
   - Minimum number of swaps
   - Works well for small arrays

5. Key disadvantages:
   - Slow for large arrays
   - Not stable
   - Doesn't adapt to input

6. Common variations:
   - Can also find maximum instead of minimum
   - Can sort in descending order (find max)

7. When asked about sorting:
   - Selection Sort for simplicity
   - Not for performance-critical code
   - Consider Merge Sort or Quick Sort for large data
"""


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    print("=" * 50)
    print("SELECTION SORT DEMO")
    print("=" * 50)
    
    # Basic test
    my_arr = [3, 7, 4, 8, 5, 2, 9, 6, 1]
    print(f"\nOriginal array: {my_arr}")
    result = selection_sort(my_arr.copy())
    print(f"Sorted array:   {result}")
    
    # Verbose version
    print("\n" + "=" * 50)
    print("STEP-BY-STEP VISUALIZATION")
    print("=" * 50 + "\n")
    selection_sort_verbose([3, 7, 4, 8, 5, 2, 9, 6, 1])
    
    # Edge cases
    print("\n" + "=" * 50)
    print("EDGE CASES")
    print("=" * 50)
    
    # Empty array
    empty = []
    print(f"\nEmpty array: {selection_sort(empty.copy())}")
    
    # Single element
    single = [1]
    print(f"Single element: {selection_sort(single.copy())}")
    
    # Two elements
    two = [2, 1]
    print(f"Two elements [2,1]: {selection_sort(two.copy())}")
    
    # Already sorted
    sorted_arr = [1, 2, 3, 4, 5]
    print(f"Already sorted: {selection_sort(sorted_arr.copy())}")
    
    # Reverse sorted
    reverse = [5, 4, 3, 2, 1]
    print(f"Reverse sorted: {selection_sort(reverse.copy())}")
    
    # With duplicates
    duplicates = [3, 1, 2, 1, 3]
    print(f"With duplicates: {selection_sort(duplicates.copy())}")