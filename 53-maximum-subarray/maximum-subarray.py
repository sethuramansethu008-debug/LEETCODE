class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        r=nums[0]
        t=0
        for i in nums:
            if t<0:
                t=0
            t+=i
            r=max(r,t)
        return r