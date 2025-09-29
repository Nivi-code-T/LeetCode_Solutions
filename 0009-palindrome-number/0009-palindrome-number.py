class Solution(object):
    def isPalindrome(self, x):
        x_str=str(x)
        y=x_str[::-1]
        if x_str==y:
            return True
        return False


        