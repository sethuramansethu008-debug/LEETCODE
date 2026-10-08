class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr=[]
        res=[]

        for c in s:
            if c=='(':
                if len(arr)!=0:
                    res.append(c)
                arr.append(c)
            else:
                arr.pop()
                if len(arr)!=0:
                    res.append(c)

        return ''.join(res)