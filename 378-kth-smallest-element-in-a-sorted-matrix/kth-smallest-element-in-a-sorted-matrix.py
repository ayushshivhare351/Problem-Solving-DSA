class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush_max(heap,matrix[i][j])
                if len(heap)>k:
                    heappop_max(heap)
        return heap[0]