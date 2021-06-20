# Validate Subsequence

## Approaches
- Naive (Time: O(nlogn), Space: O(n) )
- Two pointers (Time: O(n), Space: O(n))

## Two pointers:
- One pointer for array; One pointer for sequence
- Iterate over array if array value == sequence value => shift the sequence pointer
- If sequence pointer visit all element in sequence => return True else False 