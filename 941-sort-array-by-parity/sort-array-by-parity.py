class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            if i%2==0:
                a.append(i)
        for i in nums:
            if i%2!=0:
                a.append(i)
        return a