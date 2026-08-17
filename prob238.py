class Solution(object):
    def productExceptSelf(self, nums):


        # prefix and suffix

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        # prefix
        i = 1
        while i<len(nums):
            prefix[i] = nums[i-1]*prefix[i-1]
            i+=1


        i = len(nums)-2
        suffix[(len(nums))-1] = 1
        while i >= 0:
            suffix[i] = nums[i+1] * suffix[i+1]

            i-=1

        print(prefix)
        print(suffix)
        
        answer = [1]*len(nums)
        for i in range(len(nums)):
            answer[i] = prefix[i]*suffix[i]

        return(answer)

















        # Time limit exceeded
        # answer = []
        # for i in range(len(nums)):
        #     value = 1
        #     for j in range(len(nums)):

        #         if j !=i :
        #             value = value * nums[j]

        #     answer.append(value)
        # return answer
                

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        