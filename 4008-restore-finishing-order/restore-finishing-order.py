class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f=[]
        for i in order:
            if i in friends:
                f.append(i)
        return f
        