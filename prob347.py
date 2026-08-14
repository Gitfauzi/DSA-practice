class Solution(object):
    def topKFrequent(self, nums, k):

        #hashmap
        d = {}
         
        for key in nums:
            if key not in d:
                d[key] = 0
            d[key]+=1
        
        sorted_keys = sorted(d, key=lambda x: d[x], reverse=True)
        return sorted_keys[:k]