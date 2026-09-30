class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        max=""
        for i in range(len(num)):
            if int(num[i])%2!=0:
                max=num[:i+1]
        return max
        