class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        s=0
        for i in nums:
            if not(nums.count(i)>=2):
                s=s+i
        return s
        