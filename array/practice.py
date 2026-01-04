class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        first=nums[0]
        output = 1
        for i in nums[1:]:
            first += 1
            if first == i:
                output += 1
            # else:
            #     first = i
            #     output = 1

        if output==1:
            return 0
        return output

sol=Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))