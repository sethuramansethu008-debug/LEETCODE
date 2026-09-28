class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                x=s[i:j]
                if x==x[::-1] and len(x)>len(p):
                    p=x
        
        return p