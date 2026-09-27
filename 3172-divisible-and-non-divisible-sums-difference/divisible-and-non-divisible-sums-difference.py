class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n*(n+1)//2-m*(n//m)*(n//m+1)
        