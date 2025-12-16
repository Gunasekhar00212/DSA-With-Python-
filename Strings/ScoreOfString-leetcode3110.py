"""
Problem Name: Score of a String
Platform: LeetCode

Problem Statement:
You are given a string s. The score of the string is defined as the sum of the
absolute differences between the ASCII values of adjacent characters in the string.

Return the score of the string.

Example:
Input:  s = "abc"
Output: 2

Explanation:
|ord('a') - ord('b')| = |97 - 98| = 1
|ord('b') - ord('c')| = |98 - 99| = 1
Total score = 1 + 1 = 2

Concept Used:
- Strings
- ASCII values
- Absolute difference

Approach:
1. Initialize score = 0
2. Traverse the string from index 0 to length-2
3. For each adjacent pair of characters:
   - Convert them to ASCII using ord()
   - Add the absolute difference to score
4. Return the final score

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def scoreOfString(self, s):
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score


# Example usage (for local testing only)
solution = Solution()
print(solution.scoreOfString("hello"))  # Output: 13
