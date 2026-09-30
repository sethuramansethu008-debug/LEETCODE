class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max=0
        for i in sentences:
            l=len(i.split())
            if l>max:
                max=l
                
        return max
       
        