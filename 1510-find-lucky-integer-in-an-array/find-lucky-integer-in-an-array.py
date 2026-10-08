class Solution:
    def findLucky(self, arr: list[int]) -> int:
        r=[]
        for i in arr:
            if i==arr.count(i):
                r.append(i)
        if len(
            r)==0:
            return -1
        return max(r)

        