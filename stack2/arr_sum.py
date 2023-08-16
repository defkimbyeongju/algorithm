# 시간초과 오류 발생한 코드
# def f(i, N):
#     if i == N:
#         tmp = 0
#         for k in range(N):
#             tmp += arr[k][A[k]]
#         stack.append(tmp)
#         return
#     else:
#         for j in range(i, N): # 자신부터 오른쪽 끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     A = [i for i in range(N)]
#     stack = []
#     f(0, N)
#
#     print(f'#{tc} {min(stack)}')

'''
def dfs(level, Sum):
    global Min, path
    if level == N:  # 패를 모두 선택했다면
        if Sum < Min: # 현재 곱한 값이 최소값보다 작으면 최소값 업데이트
            Min = Sum
        return

    for i in range(N):
        for j in range(N):
        if used[i] == 1:  # 이미 사용된 패라면 건너뜀
            continue
        path.append(arr[i])  # 패를 선택하고 path에 추가
        used[i] = 1
        dfs(level+1, Sum)  # 다음 패를 선택으로 넘어가며 재귀호출
        used[i] = 0  # 복구 (백트래킹)
        path.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [] # 선택된 패들의 값을 저장할 리스트
    used = [0] * N # 패가 사용되었는지 체크
    Min = 21e8
    Sum = 0
'''

# 강사님 풀이
def dfs(idx, now_sum):
    global min_sum
    if now_sum >= min_sum: # 현재 합이 최소 합보다 크면 탐색 x
        return
    if idx == N:  # 모든 행을 선택
        if min_sum > now_sum:  # 모든 행을 선택했으면, 현재 합이 최소 합보다 작으면 최소합을 현재 합으로 업데이트
            min_sum = now_sum
            return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(idx+1, now_sum+arr[idx][i])  # 행을 다음행으로 넘어가면서 재귀 호출
            used[i] = 0 # 복구(백트래킹)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 21e8
    used=[0]*N
    dfs(0, 0)
    print(f'#{tc} {min_sum}')