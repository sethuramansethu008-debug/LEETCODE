class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def closed(i, j):  # flood the island through (i, j); True if it never reaches the border
            if not (0 <= i < m and 0 <= j < n):
                return False  # stepped off the grid: the island touches the border
            if grid[i][j]:
                return True  # water, or land we already flooded
            grid[i][j] = 1  # visited: turn it into water
            return closed(i + 1, j) & closed(i - 1, j) & closed(i, j + 1) & closed(i, j - 1)  # & (not and) floods all 4 sides

        return sum(closed(i, j) for i, j in product(range(m), range(n)) if not grid[i][j])