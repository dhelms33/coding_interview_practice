class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return 0
        if not target:
            return 0
        solution = []
        for i in range(len(nums)-1):
            if target == nums[i] + nums[i+1]:
                solution += i, i+1
        return solution
