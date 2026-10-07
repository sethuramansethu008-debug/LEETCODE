class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in set(word):
            if i.islower() and i.upper() in word:
                c+=1
        return c