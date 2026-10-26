class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        a=str(x)
        
            
        if(a==a[::-1]):
            return True
        return False

        