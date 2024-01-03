class Solution:
    # 2n개의 원소를 갖는 정수 배열
    # 그룹화한 n개의 쌍의 각 최소값의 합이 가장 큰 경우
    # 풀이:
    # 정렬 후 인접 원소끼리 그룹화 => 가장 큰 최소값 도출
    
    def arrayPairSum(self, nums: List[int]) -> int:
        group = []
        res = 0
        nums.sort()
    
        for i in range(len(nums)):
            group.append(nums[i])
            
            # group 리스트에 2개의 원소가 담겼을 때 -> 2개의 숫자를 그룹화
            if len(group) == 2:
                res += min(group[0], group[1])
                group = []
        
        return res

        
            
