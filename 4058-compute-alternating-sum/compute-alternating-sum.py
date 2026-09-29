class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        c=0
        
        for i in range(len(nums)):
            if i%2:
                c-=nums[i]
            else:
                c+=nums[i]
        return c

        