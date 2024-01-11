class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        # 중복 방문이 발생한다. == 순환 구조이다.
        traced = set()
        visited = set()

        def dfs(v):
            if v in traced:
                return False
            # 이미 방문했던 노드면 True
            if v in visited:
                return True

            traced.add(v)
            for y in graph[v]:
                if not dfs(y):
                    return False
            # 특정 경우 순환 구조가 아니지만 순환 구조로 잘못 판단하는 경우 발생
            # 이전 방문 노드는 삭제
            traced.remove(v)
            # 탐색 종료 후 방문 노드 추가
            visited.add(v)
            return True

        # 순환 구조 판별 시작
        # list(graph)로 키값 가져오기
        for x in list(graph):
            if not dfs(x):
                return False

        return True