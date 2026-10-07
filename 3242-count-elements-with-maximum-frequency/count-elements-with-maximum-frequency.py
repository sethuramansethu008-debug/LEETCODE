class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m=0
        ans=0
        for i in nums:
            if nums.count(i)>m:
                m=nums.count(i)
        for i in set(nums):
            if nums.count(i)==m:
                ans+=m
        return ans