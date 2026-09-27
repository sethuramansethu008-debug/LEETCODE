class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        r=[]
        for i in range(left,right+1):
            temp=i
            flag=True
            while(temp!=0):
                re=temp%10
                if(re==0 or i%re!=0):
                    flag=False
                    break
                temp=temp//10
            if flag:
                r.append(i)
        return r
        