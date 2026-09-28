class Solution:
    def maxDepth(self, s: str) -> int:
        d=0
        md=0
        for i in s:
            if i=='(':
                d+=1
                md=max(md,d)
            elif i==')':
                d-=1
        return md
        