class Solution(object):
    def isPalindrome(self, s):
        cleaned=""
        for i in s:
            if i.isalnum():
                cleaned += i.lower()
        
        if cleaned == cleaned[::-1]:
            return True

        else:
            return False
            
        """
        :type s: str
        :rtype: bool
        """
        