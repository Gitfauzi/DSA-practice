class Solution(object):
    def twoSum(self, nums, target):

        # cant use sets
        # if len(nums) == 1 or len(nums) == 0:
        #     pass

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        