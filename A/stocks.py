T = int(input())
for tc in range(1,T+1):
    ms, ma = map(int, input().split()) # 시드액, 월별 투자 금액
    N, L = map(int, input().split()) # 종목 수, 과거 데이터 입력 기간
    stocks = [list(map(int, input().split())) for _ in range(N)]
    temp = ms # 현재 보유 자산
    for i in range(L):
        buy = 0  # 살 종목의 개수. 날짜가 바뀔 때마다 갱신
        profit_list = []
        max_v = -21e8 # 다음 달의 가격과 비교했을 때 수익이 나는 종목의 최댓값 변수
        for j in range(N):
            add_list = []
            # 이번 달에 매수할 종목을 찾는 과정
            if stocks[j][i+1]-stocks[j][i] > 0:
                profit_list.append([stocks[j][i], stocks[j][i+1] - stocks[j][i], stocks[j][i+1]]) # 수익을 내는 애들은 리스트에 추가
        if profit_list: # 수익을 내는 애들이 있다면
            profit_list.sort(key=lambda x:(x[1], x[0]), reverse=True) # 수익을 기준으로 내림차순 정렬
            if len(profit_list) > 1:
                for k in range(len(profit_list)-1): # 순서 조정
                    for m in range(k+1, len(profit_list)):
                        x1 = profit_list[k][0]/profit_list[m][0]
                        p1 = profit_list[k][1]/profit_list[m][1]
                        if x1 > p1:
                            profit_list[k], profit_list[m] = profit_list[m], profit_list[k]
                            break


            for k in range(len(profit_list)):
                if temp > profit_list[k][0]:
                    buy = temp // profit_list[k][0]
                    add_list.append(buy*profit_list[k][2])
                    temp -= (buy*profit_list[k][0])
            temp += sum(add_list) # 이익이 있다면, 그 만큼 추가
        temp += ma # 모든 과정이 끝난 후에 다음 달에 추가될 월별 투자 금액을 더해줌
    print(f'#{tc} {temp-(ms+ma*L)}')