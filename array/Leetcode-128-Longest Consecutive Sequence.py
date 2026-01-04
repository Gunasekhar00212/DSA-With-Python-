
"""

Docstring for array.Leetcode-128-Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4
], therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


"""

class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums.sort()
        unique = list(set(nums))   # removes duplicates
        unique.sort()              # VERY IMPORTANT
        
        longest = 1
        current = 1
        
        for i in range(1, len(unique)):
            if unique[i] == unique[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        
        return max(longest, current)
