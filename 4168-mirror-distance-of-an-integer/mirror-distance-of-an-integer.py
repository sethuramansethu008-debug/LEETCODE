class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=0
        nn=n
        while(n!=0):
            a=n%10
            s=s*10+a
            n=n//10
        return abs(nn-s)

        