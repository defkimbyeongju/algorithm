'''
def serving(arr):
    for i in range(N):
        foods = [arr[i]]
        for j in range(1,r+1):
            foods.append(arr[i-j])
            if i+j < N:
                foods.append(arr[i+j])
            else:
                foods.append(arr[i+j-N])
        for i in foods:
            if foods.count(i) > 2:
                return "NO"
    return "YES"



T = int(input())
for tc in range(1,T+1):
    N, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {serving(arr)}')
'''

# 강사님 풀이

T = int(input())
for tc in range(1,T+1):
    n, r = map(int, input().split())
    foods = list(map(int, input().split()))
    arr = foods * 2 # 원형 테이블 고려
    DAT = [0] * 201 # 각 음식의 개수를 저장할 DAT
    # 시작, 끝 인덱스 초기화
    start = 0
    end = 2 * r
    flag = 0 # 서빙에 성공했는지 판단하는 변수
    # 초기 구간에서 음식의 개수를 세고, 3개 이상 중복되는지 확인
    for k in range(start, end):
        DAT[arr[k]] += 1
        if DAT[arr[k]] > 2:
            flag = 1
            break
    # 슬라이딩 윈도우 기법
    while end < 2 * n and flag == 0: # end가 리스트의 끝에 도달하거나, flag가 1이되면 종료
        DAT[arr[end]] += 1
        if DAT[arr[end]] > 2:
            flag = 1
            break
        # start 포인터가 가리키는 요소의 빈도수 1 감소
        DAT[arr[start]] -= 1
        start += 1 # start, end 1씩 증가시켜 다음 요소로 이동
        end += 1
    result = "NO" if flag else "YES"
    print(f'#{tc} {result}')