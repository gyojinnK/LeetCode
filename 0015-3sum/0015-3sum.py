class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            # 중복값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            # 간격을 좁혀가며 합 계산
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    
                    # 이해불가
                    # 설명: left, right 양 옆으로 동일한 값이 있을 수 있으므로
                    #      아래 코드를 이용해서 스킵한다.
                    # 테스트케이스를 경험하지 못해서 이해에 어려움이 있음...
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                
        return res
                    
        