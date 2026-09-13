class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        grid = []
        for item in mat:
            grid.append(item[:])
        for _ in range(k):
            for i in range(len(grid)):
                if i%2==0:
                    val = grid[i].pop(0)
                    grid[i].append(val)
                else:
                    val = grid[i].pop()
                    grid[i].insert(0,val)
        for l in range(len(grid)):
            if grid[l]!=mat[l]:
                return False
        return True