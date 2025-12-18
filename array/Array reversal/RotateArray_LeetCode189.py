Pattern Used: Array Reversal Pattern

"""
Problem Name: Rotate Array
Platform: LeetCode (Problem 189)

Problem Statement:
Given an integer array nums, rotate the array to the right by k steps,
where k is a non-negative integer.

The rotation must be done in-place, meaning you should not use extra space
for another array.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
Rotate the array 3 times to the right.

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # i=0
        # n=len(nums)-1
        # for j in range(k):
        #     nums.insert(i,nums.pop(n))
        #     # nums[i],nums[n-1]=nums[n-1],nums[i]
            
            
        # return nums
        n=len(nums)
        k=k%n

        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
