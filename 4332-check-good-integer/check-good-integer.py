class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        temp=n
        s=0
        p=1
        while(temp!=0):
            r=temp%10
            p=p+(r**2)
            s=s+r
            temp//=10
        if(p-s>=50):
            return True
        else:
            return False

        