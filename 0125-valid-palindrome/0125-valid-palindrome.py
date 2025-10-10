class Solution(object):
    def isPalindrome(self, s):
        news=""
        for char in s:
            if char.isalnum():
               news+=char.lower()
        print(news)
        
        revs=news[::-1]
        if news==revs:
            return True
        return False
        