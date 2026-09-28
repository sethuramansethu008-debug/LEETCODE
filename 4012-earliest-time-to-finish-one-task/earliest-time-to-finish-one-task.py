class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return sum(min(tasks,key=sum))

        