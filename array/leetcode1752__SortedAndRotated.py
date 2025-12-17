"""
Problem Name: Check if Array Is Sorted and Rotated
Platform: LeetCode (Problem 1752)

Problem Statement:
Given an array nums, return True if the array was originally sorted in
non-decreasing order and then rotated some number of times (possibly zero).
Otherwise, return False.

There may be duplicate elements in the array.

An array is considered rotated if it is shifted circularly.
For example, the array [1,2,3,4,5] can be rotated to become
[3,4,5,1,2].

Example 1:
Input: nums = [3,4,5,1,2]
Output: True

Example 2:
Input: nums = [2,1,3,4]
Output: False

Example 3:
Input: nums = [1,2,3]
Output: True

Explanation:
A sorted and rotated array can have at most one position where
nums[i] > nums[i+1] when checked circularly.
If such positions are more than one, the array is not valid.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""


//sol

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        breaks=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                breaks += 1
                if breaks > 1:

                    return False
        return True
         
        