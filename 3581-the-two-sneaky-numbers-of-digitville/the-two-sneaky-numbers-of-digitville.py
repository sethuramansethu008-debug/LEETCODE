class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            if nums.count(i)>=2:
                r.append(i)
        s=set(r)
        return list(s)