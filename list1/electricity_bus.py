
# 방법 1
'''
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # K: 정류장수, N: 종점, M: 충전기 설치된 정류장 수
    arr = list(map(int, input().split()))
    ch = [0] * (N+1)

    for i in arr:
        ch[i] += 1
    current = 0  # 현재 위치
    count = 0  # 충전 횟수
    while current < N:
        # 갈 수 있는 최대 거리 계산
        if ch[current + K]:
            current += K
            count += 1
        # 충전소 찾기(뒤로 한칸씩 가면서)
        else:
            for j in range(1, K):
                # 충전소를 찾으면 충전, count 증가
                if ch[current + K - j]:
                    current = current + K - j
                    count += 1
                    break
                # 충전소가 없으면, count = 0 반복 종료
            else:
                count = 0
                break
        # 최대거리가 도착점보다 멀거나 같으면, 반복 종료
        if current + K >= N:
            current = N
    print(f'#{tc} {count}')
'''

# 방법 2
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # K: 정류장수, N: 종점, M: 충전기 설치된 정류장 수
    arr = list(map(int, input().split()))
    # curr : 현재 위치, cnt : 충전횟수
    curr, cnt = 0, 0
    # 종점 도착할 때까지 반복
    while curr != N:
        # curr+K : 한 번 충전으로 갈 수 있는 거리, N: 종점까지 거리
        if N <= curr + K:
            curr = N
            break
        # 충전소 뒤에서부터 순회    
        for i in range(len(arr)-1, -1, -1):
            # 리스트 arr의 값이 curr+K(한번 충전으로 갈 수 있는 거리) 거리 이내에 있다면
            if arr[i] <= curr + K:
                cnt += 1 # 충전 횟수 증가
                curr = arr[i] # 현재 위치를 충전소 위치로 변경
                arr = arr[i+1:] # 해당 충전소 이후의 정류장만 남기기
                break
            # 충전소를 찾지 못했다면
            if i == 0:
                cnt = 0
                curr = N # 현재 위치를 종점으로
        d = 1 # 디버깅시 실행코드가 없는 경우 dummy code를 중단점으로 활용
    print(f'#{tc} {cnt}')
        



# 내 풀이

# 헤맸던 이유: 충전소가 없으면 count = 0, 반복 종료를 어떻게 구현할지 잘 몰라서 헤맸다. 알고보니, 가장 바깥쪽 if문에 else로 설정해줬으면 쉽게 해결될 수 있었음.
'''
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    bus_stop = [0] * (N+1)
    charge_time = 0 # 충전횟수 카운트
    cnt = 0 # bus_stop 인덱스로 접근하기 위한 변수 설정
    for i in arr: # 충전소가 있는 곳은 1로 표시하는 bus_stop 리스트
        bus_stop[i] += 1
    bus_stop[0] = 1 # 일단 1로 하고 나중에 빼주기
    while True: # 반복문
        if cnt >= N: # cnt가 정류장 길이를 넘기면 반복문 종료
            break
        if bus_stop[cnt] == 1:
            charge_time += 1
        else:
            for j in range(1, K):
                if bus_stop[K + cnt - j] == 1:
                    charge_time += 1
                    cnt += K - j
                    break


        if charge_time == 0:
            break

    print(f'#{tc} {charge_time}')
'''