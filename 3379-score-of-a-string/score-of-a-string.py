class Solution:
    def scoreOfString(self, s: str) -> int:
        ss=0
        for i in range(1,len(s)):

            ss+=abs(ord(s[i-1])-ord(s[i]))
        return ss
        