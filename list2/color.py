
''' 정답코드
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 10x10 격자 생성
    arr = [[0] * 10 for _ in range(10)]
    result = 0
    for k in range(N):
        red1, blue1, red2, blue2, color = map(int,input().split())

        for i in range(red1, red2 +1):
            for j in range(blue1, blue2+1):
                arr[i][j] += color
                # 격자 값이 3이면 카운팅
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 10x10 격자 생성
    arr = [[0]*10 for _ in range(10)]
    result = 0
    for k in range(N):
        r1, b1, r2, b2, color = map(int, input().split())# 칠할 영역에 대한 값을 3번 입력 받음
        for i in range(r1, r2+1):
            for j in range(b1, b2+1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')


