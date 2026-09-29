class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max=0
        for i in sentences:
            if len(i.split())>max:
                max=len(i.split())
                
        return max
       
        