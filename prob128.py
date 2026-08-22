class Solution(object):
    def longestConsecutive(self, nums):


        # using hashset
        nums_set = set(nums)
        max_count = 0
        count = 0
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        for nums in nums_set:
            if nums-1 not in nums_set:
                count = 1
                while nums+count in nums_set:
                    count +=1
                max_count = max(max_count, count)
            
        return max_count
                
        

        # not the best approach
        # nums.sort()

        # max_count = 0
        # count = 1
        # if len(nums)==0:
        #     return 0
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]: #duplicate
        #         continue

        #     elif nums[i-1] == nums[i]-1:
        #         count+=1
        #         max_count = max(max_count,count)
        #     else:
        #         count = 1
        # return max(max_count, count)


        """
        :type nums: List[int]
        :rtype: int
        """
        