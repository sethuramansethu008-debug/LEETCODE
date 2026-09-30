class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a=0
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        if k>len(l):
            return -1
        else:
            return l[k-1]
        