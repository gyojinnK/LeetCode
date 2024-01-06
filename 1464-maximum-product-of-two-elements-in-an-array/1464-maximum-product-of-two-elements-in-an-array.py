class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = []
        mul = 0
        for el in nums:
            heapq.heappush(max_heap, -el)

        mul = (heapq.heappop(max_heap) + 1) * (heapq.heappop(max_heap) + 1)
        return mul
