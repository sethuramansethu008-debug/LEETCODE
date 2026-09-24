class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums[i]
            t=0
            while x>0:
                t+=x%10
                x=x//10
            if t==i:
                return i
        return -1
        