## Problem 1 — Find Peak Element

### Problem Statement
Given an array of integers, return the index of any peak element.  
A peak element is greater than its neighbors.

### Example
Input: [1,2,3,4,3,2]  
Output: 3

### Approach
Binary search to compare mid with mid+1 and move toward the increasing direction.

### Complexity
Time: O(log n)  
Space: O(1)
