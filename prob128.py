class Solution(object):
    def longestConsecutive(self, nums):
        # not the best approach
        nums.sort()

        max_count = 0
        count = 1
        if len(nums)==0:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]: #duplicate
                continue

            elif nums[i-1] == nums[i]-1:
                count+=1
                max_count = max(max_count,count)
            else:
                count = 1
        return max(max_count, count)


        """
        :type nums: List[int]
        :rtype: int
        """
        