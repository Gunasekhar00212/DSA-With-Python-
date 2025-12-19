class Solution(object):
    def moveZeroes(self, nums):
        """
        Problem Statement:
        Given an integer array nums, move all 0's to the end of the array
        while maintaining the relative order of the non-zero elements.

        You must do this in-place without making a copy of the array.

        Example:
        Input:  nums = [0, 1, 0, 3, 12]
        Output: nums = [1, 3, 12, 0, 0]

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
