class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        c=0
        for i in grid:
            for j in i:
                if j<0:
                    c+=1
        return c
        