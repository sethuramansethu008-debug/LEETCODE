class Solution:
    def findMin(self, nums: list[int]) -> int:
        nums.sort()
        return nums[0]