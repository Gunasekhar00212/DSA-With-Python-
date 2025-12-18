"""
Problem Name: Remove Duplicates from Sorted Array
Platform: LeetCode (Problem 26)

Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.

The relative order of the elements should be kept the same.

Return the number of unique elements k.
The first k elements of nums should contain the unique elements.
The remaining elements beyond index k - 1 are not important.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order

Example:
Input: nums = [1,1,2]
Output: 2
nums becomes [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
nums becomes [0,1,2,3,4,_,_,_,_,_]
"""


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  # slow pointer

        for j in range(1, len(nums)):  # fast pointer
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
