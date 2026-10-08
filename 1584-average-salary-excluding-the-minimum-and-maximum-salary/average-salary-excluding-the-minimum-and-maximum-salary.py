class Solution:
    def average(self, salary: list[int]) -> float:
        maxx=max(salary)
        minn=min(salary)
        l=[]
        for i in salary:
            if i!=maxx and i!=minn:
                l.append(i)
        return sum(l)/len(l)
        