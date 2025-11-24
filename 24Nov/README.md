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


## Problem 2 — Roman to Integer

### Problem Statement
Given a string representing a Roman numeral, convert it into its integer value.
Roman numerals use combinations of letters from the Latin alphabet where smaller values placed before larger values indicate subtraction.

### Example
Input: "MCMXCIV"
Output: 1994

### Approach
Use a mapping dictionary for each Roman symbol and iterate through the string.
If a numeral is smaller than the next one (e.g., I before V), subtract it — otherwise add it normally.

### Complexity
Time: O(log n)  
Space: O(1)
