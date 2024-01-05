class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 탐색을 위한 투포인터
        checker = []
        head = rear = longest = 0
        
        while rear < len(s):
            # 중복(재등장) 확인을 위함
            if s[rear] in checker:
                longest = max(longest, len(checker))
                checker = []
                # 다음 문자부터 다시 탐색
                head += 1
                rear = head
            else:
                # 중복이 없다면 리스트에 적재
                checker.append(s[rear])
                # 현재 리스트의 길이(중복이 없는 긴문자열 일 경우 정답) 저장
                longest = max(longest, len(checker))
                rear += 1
        return longest