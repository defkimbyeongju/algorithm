T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    ans = 0 # 단어가 들어갈 수 있는 자리의 수
    for i in range(N):  # 행 우선 순회
        count = 0 # 연속한 빈칸(1)의 개수
        for j in range(N):
            if arr[i][j]:
                count += 1
            if j==N-1 or arr[i][j] == 0:
                if count == K:
                    ans += 1
                count = 0
    for k in range(N):  # 열 순회
        cnt = 0
        for p in range(N):
            if arr[p][k]:
                cnt += 1
            if p==N-1 or arr[p][k] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{tc} {ans}')
