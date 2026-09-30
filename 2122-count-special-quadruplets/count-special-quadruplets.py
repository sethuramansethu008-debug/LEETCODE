class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i]+nums[j]+nums[k]==nums[l]:
                            c+=1

        return c