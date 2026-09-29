class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=set(nums)
        r=[]
        for i in range(min(nums),max(nums)+1):
            if i not in l:
                r.append(i)
        return r
        