class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nn=n
        nnn=n
        s=0
        p=1
        while(n!=0):
            a=n%10
            s=s+a
            n=n//10
        while(nn!=0):
            b=nn%10
            p=p*b
            nn=nn//10
        return p-s


        