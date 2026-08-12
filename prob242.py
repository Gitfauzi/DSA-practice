class Solution(object):
    def isAnagram(self, s, t):
        # BELOW working
        s_list = list(s)
        new_s = sorted(s_list)

        t_list = list(t)
        new_t = sorted(t_list)

        if new_s == new_t:
            return True
        return False

        # NOT WORKING
        # if len(s) == len(t):
        #     s_set = set(s)
        #     t_set = set(t)
        # else:
        #     return False
            
        # if s_set == t_set:
        #     return True
        # else:
        #     return False

        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        