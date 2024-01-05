class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        res = []
        
        h = []
        for num in counter:
            heapq.heappush(h, [-counter[num], num])

        for _ in range(k):
            poped = heapq.heappop(h)
            res.append(poped[1])

        return sorted(res)
        