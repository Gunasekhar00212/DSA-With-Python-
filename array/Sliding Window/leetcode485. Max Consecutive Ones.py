class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Problem Statement:
        Given a binary array nums, return the maximum number of consecutive 1's in the array
        Example:
        Input: nums = [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    
        :type nums: List[int]
        :rtype: int

        """
        # i=0
        
        # count=1
        # max_count=1
        # for j in range (1,len(nums)):
        #     if nums[i]==nums[j]==1:
        #         count +=1
        #         max_count=max(count,max_count)
        #     else:
        #         count=1 if nums[j] ==1 
        #     i += 1
        # return max_count
        count =0
        max_count=0
        for num in nums:
            if num==1:
                count += 1
                max_count=max(count,max_count)
            else:
                count=0
        return max_count
        