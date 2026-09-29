class Solution:
    def xorOperation(self, a: int, b: int) -> int:
        s=0
        for i in range(a):
            s=s^b
                
            b=b+2
        return s
        