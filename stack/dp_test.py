# def fibo(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
# print(fibo(100))

# dfs 연습문제
'''
V E
v1 w1 v2 w2 ...
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

입력 방식은 인접 행렬, 인접 리스트 등이 있음
'''
# 출력 결과는 1-2-4-6-5-7-3

def dfs(n, V, adj_m):
    stack = []   # stack 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1      # 시작점 방문 표시
    print(n)         # do[n]
    while True:
        for w in range(1, V+1):    # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v), v = w
                n = w
                print(n)        # do(w)
                visited[n] = 1  # w방문 visited
                break  # for w, n 에 인접인 w c 찾은 경우
        else:
            if stack:  # stack에 지나온 정점이 남아있으면
                n = stack.pop()  # pop()해서 다시 다른 w 찾을 n 준비
            else:
                break # while True 탐색 끝


V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

dfs(1, V, adj_m)
