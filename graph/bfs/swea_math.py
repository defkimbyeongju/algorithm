from collections import deque

def bfs(n, m):
    queue = deque([(n, 0)])  # 큐에 (숫자, 이동 횟수)를 함께 저장
    visited = set()  # 이미 방문한 숫자를 추적하기 위한 집합
    visited.add(n)

    while queue:
        t, cnt = queue.popleft()

        if t == m:
            return cnt

        # 가능한 모든 이동을 확인하고 방문하지 않은 숫자를 큐에 추가
        possible_moves = [t + 1, t - 1, t * 2, t - 10]
        for move in possible_moves:
            if move not in visited and move < 1000**2+1:
                visited.add(move)
                queue.append((move, cnt + 1))

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    res = bfs(N, M)
    print(f'#{tc} {res}')