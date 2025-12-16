"""
LeetCode 303 - Range Sum Query - Immutable

Problem:
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive.

Example:
nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Constraints:
- Multiple sumRange queries
- Array does not change
"""


class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0] * len(nums)

        if nums:
            self.prefix[0] = nums[0]
            for i in range(1, len(nums)):
                self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


"""
Approach:
Prefix Sum

Time Complexity:
- Preprocessing: O(n)
- Query: O(1)

Space Complexity:
O(n)
"""

