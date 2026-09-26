class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        nn=num
        while(nn>0):
            a=nn%10
            if(num%a==0):
                c+=1
            nn//=10
        return c
