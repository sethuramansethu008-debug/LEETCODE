class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        def expand(l,r):
            re=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                re+=1
                l-=1
                r+=1
            return re
        for i in range(len(s)):
            c+=expand(i,i)
            c+=expand(i,i+1)
        return c
            