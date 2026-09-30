class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        aa=set(a)
        for i in aa:
            if a.count(i)>b.count(i):
                return False

        return True