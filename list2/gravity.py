''' 정답코드
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    # 방의 가로 길이만큼 반복
    for i in range(N):
        cnt = 0
        # 현재 위치의 오른쪽에 있는 모든 상자를 확인
        for j in range(i+1, N):
            # 현재 위치의 상자가 오른쪽의 상자보다 높이가 크면
            if arr[i] > arr[j]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')
'''


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')