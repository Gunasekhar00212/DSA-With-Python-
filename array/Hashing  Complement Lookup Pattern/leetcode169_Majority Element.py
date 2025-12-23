"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_value=max(nums)
        # count =[0]*(max_value+1)
        # for num in nums:
        #     count[num] += 1
        # for i in range(len(count)):
        #     if count[i] > len(nums)/2:
        #         return i
        freq = {}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            if value > len(nums) //2:
                return key
            

        