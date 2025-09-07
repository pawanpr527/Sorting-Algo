| Algorithm      | Best Case  | Average Case | Worst Case | Space    | Stable?                        |
| -------------- | ---------- | ------------ | ---------- | -------- | ------------------------------ |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅                              |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      | O(1)     | ✅                              |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      | O(1)     | ❌                              |
| **Heap Sort**  | O(n log n) | O(n log n)   | O(n log n) | O(1)     | ❌                              |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) | O(n)     | ✅                              |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      | O(log n) | ❌                              |
| Counting Sort  | O(n + k)   | O(n + k)     | O(n + k)   | O(k)     | ✅                              |
| Radix Sort     | O(nk)      | O(nk)        | O(nk)      | O(n + k) | ✅                              |
| Bucket Sort    | O(n + k)   | O(n + k)     | O(n²)      | O(n + k) | ✅ (if stable sort used inside) |


1. Stable Sort

A sorting algorithm is stable if it preserves the relative order of equal elements.
👉 If two elements are equal, they appear in the same order in the sorted array as they were in the input.

Example:
List of students with (name, marks):

[ ("Alice", 90), ("Bob", 90), ("Charlie", 85) ]


Sort by marks (ascending).

A stable sort will keep Alice before Bob (because Alice appeared first in the input).
Result:

[ ("Charlie", 85), ("Alice", 90), ("Bob", 90) ]

2. Unstable Sort

An unstable sort does not guarantee preserving the order of equal elements.
👉 Equal elements may change their relative positions after sorting.

Same example:

[ ("Alice", 90), ("Bob", 90), ("Charlie", 85) ]


An unstable sort might output:

[ ("Charlie", 85), ("Bob", 90), ("Alice", 90) ]


Bob and Alice swapped order even though both have 90.
