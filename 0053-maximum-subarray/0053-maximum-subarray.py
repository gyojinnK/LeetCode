class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        start = 1
        while start < len(nums):
            target = nums[start]
            acc = dp[-1]
            if target > target + acc:
                dp.append(target)
                start += 1
            else:
                dp.append(target + acc)
                start += 1

        return max(dp)