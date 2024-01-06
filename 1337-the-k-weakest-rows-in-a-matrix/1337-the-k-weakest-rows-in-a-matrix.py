class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        res = []

        for i, el in enumerate(mat):
            soldiers = el.count(1)
            # 군인의 수, 인덱스 순서로 리스트에 저장
            min_heap.append([soldiers, i])
        
        # 리스트를 힙으로 전환
        # 최소 힙
        heapq.heapify(min_heap)
        
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res