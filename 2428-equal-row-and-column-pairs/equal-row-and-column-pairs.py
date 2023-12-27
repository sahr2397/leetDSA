from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = defaultdict(int)
        for row in grid:
           m[tuple(row)] += 1
        count = 0
        for col in zip(*grid):
            count += m[tuple(col)]
        return count