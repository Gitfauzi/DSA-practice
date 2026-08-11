class Solution(object):
    def missingInteger(self, nums):
        count = 0
        sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]-1:
                count+=1
                actual = count
                sum = sum + nums[i]
                if actual >= count:
                    finalsum = sum
            else:
                count = 0
        
        for i in range(len(nums)):
            if nums[i] == finalsum:
                pass
            else:
                return finalsum


        

        """
        :type nums: List[int]
        :rtype: int
        """
        