# Smallest difference

## Approaches:
- Two pointers ( Time: O(nlogn + mlogm), Space: O(1))


### Two pointer approach
- Sorted two arrays
- Try to keep difference near 0 as many as possible:
- If n1 < n2 => shift n1 to bigger value
- If n2 < n1 => shift n2 to bigger value
- If n1 == n2 => return immediately [n1, n2] because the minimum diff is 0
