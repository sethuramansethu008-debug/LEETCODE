class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        return a
        