# Problem: Determine Valid Binary Array from Derived Array

## Problem Statement

You are given a 0-indexed array `derived` of length `n`, which is created by computing the bitwise XOR (⊕) of adjacent values in a binary array `original` of length `n`.

For each index `i` in the range `[0, n - 1]`:
- If `i = n - 1`, then `derived[i] = original[i] ⊕ original[0]`.
- Otherwise, `derived[i] = original[i] ⊕ original[i + 1]`.

Your task is to determine whether there exists a valid binary array `original` that could have formed `derived`.

Return `true` if such an array exists, or `false` otherwise.

A binary array is an array containing only `0`s and `1`s.

### Example 
```plaintext
Input: derived = [1, 1, 0]
Output: true
Explanation: A valid original array that gives derived is [0, 1, 0].
derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
```

[Link to the challenge](https://leetcode.com/problems/neighboring-bitwise-xor/description/)
