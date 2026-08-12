class Solution(object):
    def containsDuplicate(self, nums):

        # BELOW works
        #  t.c = On
        # sc = On (extra space for set)     
        # my_set = set(nums)
        # if len(my_set) == len(nums):
        #     return False
        # else:
        #     return True
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # BELOW also works
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        
        # NOT WORKING
        # if len(nums) == 1 or len(nums) == 0:
        #     return False
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
            
        # return False