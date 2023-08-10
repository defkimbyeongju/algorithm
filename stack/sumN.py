# N = int(input())
#
# def sumN(n):
#     if (n//10) == 0:
#         return n
#     else:
#         return sumN(n//10) + (n%10)
#
# print(sumN(N))


card = list(input())
path = [0]*4
cnt = 0

def card_cnt(level): # level은 현재 뽑은 카드의 수
    global cnt
    # 4장의 카드를 뽑았으면 경우의 수 증가
    if level == 4:
        cnt += 1
        return # 재귀 호출 종료
    for i in range(5):
        path[level] = card[i]  # 현재 레벨 경로에 선택한 카드를 저장
        # 연속된 카드 간의 차이가 4이상이면 다음카드를 선택 -> 백트래킹!!
        if int(path[level]) - int(path[level-1]) >= 4:
            continue
        if int(path[level-1]) - int(path[level]) >= 4:
            continue
        # 다음 레벨로 재귀 호출
        card_cnt(level+1)
card_cnt(0)
print(cnt)