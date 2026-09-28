class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        r=[]
        for i in range(len(tasks)):
            r.append(sum(tasks[i]))
        return min(r)

        