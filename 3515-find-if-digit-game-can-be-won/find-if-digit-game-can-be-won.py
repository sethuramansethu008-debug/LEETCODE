class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a=0
        b=0
        for i in nums:
            if i<10:
                a+=i
            else:
                b+=i
        return a!=b
        