class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        a=len(set(candyType))
        b=len(candyType)//2
        
        return min(a,b)        