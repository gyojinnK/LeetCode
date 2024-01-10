class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] # 순열 조합이 완성되면 저장
        path = [] # 각 재귀 호출 마다 순열 저장

        def dfs(nums):
            # 요소가 없다 == 다음 dfs 수행할 요소가 없다
            if len(nums) == 0:
                res.append(path[:])

            for e in nums:
                # next: 다음 dfs를 수행할 다음 요소들
                next = nums[:]
                next.remove(e)

                # path에 하나씩 적재
                path.append(e)
                # 다음 요소들로 다시 dfs ㄱㄱ
                dfs(next)
                path.pop()

        dfs(nums)
        return res