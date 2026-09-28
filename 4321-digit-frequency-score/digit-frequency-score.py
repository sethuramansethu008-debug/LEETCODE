class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=0
        while n>0:
            r=n%10
            s=s+r
            n=n//10
        return s

        