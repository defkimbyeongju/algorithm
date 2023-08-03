N, M = map(int, input().split())
fire = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

dir = [(0, 1), (0,-1), (-1,0), (1,0)]

for i in range(N):
    for j in range(M):
        # 이중 리스트 요소들을 하나씩 순회하면서 폭탄 확인
        if arr[i][j] == "@":
            # 방향 설정(동, 서, 남, 북)
            for k, p in dir:
                # 화력 설정(1부터 시작)
                for a in range(1, fire+1):
                    # arr에 접근할 인덱스 설정. ny, nx
                    ny, nx = i + (k*a), j + (p*a)
                    # 0이상 N, M 이하. 범위 안에 들어와야 됨
                    if 0 <= ny < N and 0 <= nx < M:
                        # 멀쩡한 땅일 때만 폭탄의 영향을 받음
                        if arr[ny][nx] == "_":
                            arr[ny][nx] = "%"
                        # 여기가 중요!!!!! continue가 아닌 break를 써줘야 함! 그 이유는 continue를 쓰면 벽을 뚫어버림.
                        if arr[ny][nx] == "#":
                            break
            arr[i][j] = "%"
for row in arr:
    print(*row)



