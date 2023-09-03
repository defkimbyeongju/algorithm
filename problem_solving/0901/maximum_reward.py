T = int(input())
for tc in range(1, T+1):
    num, exchange = input().split()
    exchange = int(exchange)
    now = set([num]) # 숫자판 조합을 담는 집합
    next = set()  # 다음 턴
    for _ in range(exchange): # 교환 횟수만큼 숫자판 자리 교환
        while now: # 현재 가능한 모든 숫자판 조합 확인
            s = now.pop() # 하나의 숫자판 조합을 가져오고, 리스트로 변환
            s = list(s)
            # 숫자판의 모든 자리를 서로 교환
            for i in range(len(num)-1):
                for j in range(i+1, len(num)):
                    # 1. 두자리를 서로 교환
                    s[i], s[j] = s[j], s[i]
                    # 교환한 결과를 next 집합에 추가
                    next.add(''.join(s))
                    # 2. 다시 원래대로
                    s[i], s[j] = s[j], s[i]
        now, next = next, now # 현재 집합과 next 집합 교환
    result = max(map(int, now))
    print(f'#{tc} {result}')