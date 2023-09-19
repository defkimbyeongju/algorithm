# def backtracking(now, change):
#     global min_v
#     if now >= N:
#         if change < min_v:
#             min_v = change
#         return
#     if change >= min_v:
#         return
#     for i in range(1, battery[now-1]+1):
#         backtracking(now+i, change+1)
#
# T = int(input())
# for tc in range(1,T+1):
#     min_v = 21e8
#     input_list = input().split()
#     N, *battery = map(int, input_list)
#     backtracking(1, 0)
#     print(f'#{tc} {min_v-1}')

# 강사님 풀이

def dfs(idx, sum_v):
    global answer
    # 현재 교환 횟수가 이미 찾은 정답보다 많으면 탐색 종료(백트래킹)
    if answer < sum_v: return
    # 현재 위치가 종점 이상이면 종점에 도달한 것이므로 최소 교환 횟수 갱신, 종료
    if idx >= N:
        answer = sum_v
        return
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx+i, sum_v+1)
T = int(input())
for tc in range(1,T+1):
    answer = float('inf')
    station = list(map(int, input().split()))
    N = station.pop(0) - 1 # 첫번째 값은 정류장의 수, 따로 저장, 나머지는 배터리 정보로 사용
    dfs(0, -1)
    print(f'#{tc} {answer}')