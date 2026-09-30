class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        o=['(','[','{']
        c=[']',')','}']
        for i in s:
            if i in o:
                a.append(i)
            else:
                if len(a)==0:
                    return False
                if i==')' and a[-1]!='(':
                    return False
                if i==']' and a[-1]!='[':
                    return False
                if i=='}' and a[-1]!='{':
                    return False
                a.pop()

        if len(a)==0:
            return True
        else:
            return False