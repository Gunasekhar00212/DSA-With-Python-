"""
Problem Name: Missing Number
Platform: LeetCode (Problem 268)

Problem Statement:
Given an array nums containing n distinct numbers in the range [0, n],
return the one number that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Explanation:
The array contains all numbers from 0 to n except one.
Using the XOR operation:
- XOR of a number with itself is 0
- XOR of a number with 0 is the number itself
By XORing all numbers from 0 to n and all elements in the array,
the missing number remains.

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in nums are unique
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        n=len(nums)
        for i in range(n+1):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor