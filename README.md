# Basic Sorting Algorithms

## Bubble Sort:

> **Strategy**: Simple Comparison

> **Description**: Repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. This process continues until no more swaps are needed, which indicates that the list is sorted. The algorithm gets its name because smaller elements "bubble" to the front of the list, while larger elements "sink" to the end of the list with each pass.

> **Algorithm**:

1.  Iterate over each element of the array with index_i (outer loop)
2.  Iterate from left to the array length minus index_i - 1 (since the last elements are already in place)(inner loop)
3.  Compare the current value with the adjacent one. If it's greater - swap.

> **Time & Space Complexity**:

| Performance       | Complexity |
| ----------------- | ---------- |
| Worst-case time   | O(n^2)     |
| Best-case time    | O(n)       |
| Average-case time | O(n^2)     |
| Space             | O(1)       |

---

## Selection Sort:

> **Strategy**: Simple Comparison

> **Description**: Sorts an array by repeatedly finding the minimum element from the unsorted part of the array and placing it at the beginning of the array. The algorithm maintains two subarrays in the given array: the sorted subarray, which is built up from left to right at the beginning of the array, and the unsorted subarray, which contains the remaining unsorted elements.

> **Algorithm**:

1.  Assume the first element of the array is the minimum element.
2.  Traverse the array from the second to the last element.
3.  Compare each element with the current minimum. Update accordingly.
4.  After completing one pass swap the minimum element with the first element in the array.
5.  Repeat step 2-4 for the remaining unsorted array.

> **Time & Space Complexity**:

| Performance       | Complexity |
| ----------------- | ---------- |
| Worst-case time   | O(n^2)     |
| Best-case time    | O(n^2)     |
| Average-case time | O(n^2)     |
| Space             | O(1)       |

---

## Quick Sort:

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
