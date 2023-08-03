''' 개 쓰레기 같은 코드
bingo = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]

bingo_num = 0

while True:
    for i in range(5):
        for j in range(5):
            ans = mc[i][j]
            for k in range(5):
                for p in range(5):
                    if bingo[k][p] == ans:
                        bingo[k][p] = "_"
                        if bingo[k][0] == bingo[k][1] == bingo[k][2] == bingo[k][3] == bingo[k][4]:
                            bingo_num += 1
                        if bingo[0][p] == bingo[1][p] == bingo[2][p] == bingo[3][p] == bingo[4][p]:
                            bingo_num += 1
                        if k == p:
                            if bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4]:
                                bingo_num += 1
                        if bingo[4][0] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[0][4]:
                            bingo_num += 1
                    if bingo_num == 3:
                        break
                if bingo_num == 3:
                    break
            if bingo_num == 3:
                break
        if bingo_num == 3:
            break
    if bingo_num == 3:
        print(ans)
        break
'''

# 강사님 코드

'''
board = [int(num) for _ in range(5) for num in input().split()]
call = [int(num) for _ in range(5) for num in input().split()]  # 일차원 리스트로 받음. 그럼 반복문을 몇 중으로 돌릴 필요가 없어짐!
cnt = 0

# 가로, 세로, 대각선 빙고를 체크하기 위한 리스트 생성
x_list = [0] * 10
y_list = [0] * 10
di_list1 = [0] * 10
di_list2 = [0] * 10

for n in call:
    # 부른 숫자의 인덱스 찾기
    a = board.index(n)
    # 인덱스를 이용해 해당 숫자의 위치 x,y 계산
    x,y = a//5, a % 5
    # 가로, 세로, 대각선 빙고 개수 카운트 증가
    x_list[x] += 1
    y_list[y] += 1
    di_list1[x+y] += 1
    di_list2[y - x+4] += 1
    # 빙고 개수를 확인하여 count 증가
    if x_list[x] == 5:
        cnt += 1
    if y_list[y] == 5:
        cnt += 1
    if di_list1[x+y] == 5 or di_list2[y-x+4] == 5:
        cnt += 1
    if cnt == 3:
        print(n)
        break
'''

# 다시 한 번 풀어본다

bingo = [int(num) for _ in range(5) for num in input().split()]
mc = [int(num) for _ in range(5) for num in input().split()]

bingo = []
mc = []
for _ in range(5):
    for num in input().split():
        bingo.append(int(num))
for _ in range(5):
    for num in input().split():
        mc.append(int(num))

for i in mc:
    a()