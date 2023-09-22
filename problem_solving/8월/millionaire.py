# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     price = list(map(int,input().split()))
#     max_v = max(price)
#     max_idx = price.index(max_v)
#     temp = 0
#     total = 0
#     while max_idx < len(price) -1 :



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = 0
    price = list(map(int, input().split()))
    max_v = price[N-1]
    for i in range(N-2,-1,-1): # 오른쪽에서부터 시작해서 max 값을 바꿔가며, 합을 구하는 방식
        ans += max((max_v - price[i]),0)
        max_v = max(price[i], max_v)
    print(f'#{tc} {ans}')