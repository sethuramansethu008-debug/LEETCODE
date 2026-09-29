class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s=0
        d=0
        for i in nums:
            s=s+i
        for i in nums:
            if i>9:
                for j in str(i):
                    d=d+int(j)
            else:
                d=d+i
        return s-d


        