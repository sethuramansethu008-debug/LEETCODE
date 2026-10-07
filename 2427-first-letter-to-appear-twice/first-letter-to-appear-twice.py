class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sett=set()
        for i in s:
            if i in sett:
                return i
            sett.add(i)