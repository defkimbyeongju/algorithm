T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int, input().split())  # N 손님수, M초마다 K개 생산
    guest = list(map(int, input().split()))  # N명 도착 시간
    guest.sort()
    result = 'Possible'
    for i in range(N):
        if i+1  > guest[i]//M*K:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')