class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        r=0
        for i in accounts:
            r=max(r,sum(i))
        return r

        