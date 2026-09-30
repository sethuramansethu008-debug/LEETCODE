class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        for i in a:
            if a.count(i)>b.count(i):
                return False

        return True