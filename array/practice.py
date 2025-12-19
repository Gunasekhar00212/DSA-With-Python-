class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n1=len(nums)
        nums=[x for x in nums if x != 0]
        n2=len(nums)
        zeros=n1-n2
        i=0
        while i < zeros:
            nums.append(0)
            i += 1
        return nums

sol=Solution()
print(sol.moveZeroes([0,1,0,3,12]))  # Output