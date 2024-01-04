class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tem = temperatures
        res = [0] * len(tem)
        stack = []
        # 인덱스를 이용해서 연산
        # tem의 원소(온도)를 인덱스와 함께 반복
        for i, t in enumerate(tem):
            # 스택이 비어있지 않고
            # 현 온도가 이전 스택에 적재한 인덱스의 온도보다 높다면
            while stack and t > tem[stack[-1]]:
                # 스택에 적재된 상위 인덱스를 pop
                target = stack.pop()
                # 결과 리스트의 해당 인덱스에 현 인덱스와 스택에 적재된 상위 인덱스의 차를 저장
                res[target] = i - target
            # while문 조건에 해당되지 않으면 현 온도의 인덱스 저장
            stack.append(i)

        return res