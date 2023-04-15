# Basic Sorting Algorithms

## Quick-Sort:

> **Strategy**: Divide & Conquer

> **Description**: Picks an element as a pivot and partitions the given array around the picked pivot. Selection of pivot can be done in different ways (always pick the first, the last, a random element, or median). The target of `partion` is to put the pivot at its correct position in a sorted array and put all smaller elements before, and all greater elements after the pivot. This should be done in linear time.

> **Algorithm**:

1.  As long as starting index is less than ending index
2.  Partition the array in place and return pivot index
    1.  Select the last value of the array as the pivot
    2.  Set a pointer to the left index - 1
    3.  Iterate over the array from left to right
    4.  If the current value is smaller than the pivot increase the left-pointer by one and swap.
    5.  Swap the pivot in the correct position
    6.  Return the pointer
3.  Call quick-sort recursively on the left and right subarray

> **Time & Space Complexity**:

| Case         | Time Complexity | Space Complexity |
| ------------ | --------------- | ---------------- |
| Best-case    | O(n\*log(n))    | O(log(n))        |
| Worst-case   | O(n^2)          | O(n)             |
| Average-case | O(n\*log(n))    | O(log(n))\*      |

---
