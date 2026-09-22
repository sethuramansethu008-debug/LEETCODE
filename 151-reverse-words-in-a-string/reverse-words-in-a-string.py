class Solution:
    def reverseWords(self, s: str) -> str:
        ss=s.split()
        return " ".join(ss[::-1])
        
        
        