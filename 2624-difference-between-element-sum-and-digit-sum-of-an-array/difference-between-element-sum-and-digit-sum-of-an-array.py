class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=0
        t=0
        for i in nums:
            s+=i
        for j in nums:
            while j > 0:
                t+=j%10  
                j=j//10
        return(abs(s-t))
        
        