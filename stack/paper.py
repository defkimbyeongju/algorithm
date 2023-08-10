
def paper(n):
    if n % 10 == 0:
        if n == 10:
            return 1
        elif n == 20:
            return 3
        else: # 30이상
            return paper(n-10) + (2*paper(n-20))


T = int(input())
for tc in range(1,T+1):
    N= int(input())
    print(f'#{tc} {paper(N)}')
