def perm(L):
    if L == M:
        print(*result)
    else:
        for i in range(N):
            if check[i] == 0:
                result[L] = num[i]
                check[i] = 1
                perm(L+1)
                check[i] = 0


N,M = map(int, input().split())
num = [i+1 for i in range(N)]
result = [0]*M
check = [0]*N
perm(0)