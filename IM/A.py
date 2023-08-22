T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    idx_lst = [i for i in range(N)]
    abcd = []
    max_v = 0
    for i in range(N):
        idx_lst2 = idx_lst.copy()
        idx_lst2.remove(i)
        idx_lst2.remove(idx_lst2[i-1])
        idx_lst2.remove(idx_lst2[(i+1)%N])
        if (i+2//N) % N in idx_lst2:
            idx_lst2.remove(idx_lst2[(i+2//N)%N])
        for j in idx_lst2:
            idx_lst3 = idx_lst2.copy()
            idx_lst3.remove(j)
            if j-1 in idx_lst3:
                idx_lst3.remove(j-1)
            if j+1 in idx_lst3:
                idx_lst3.remove(j+1)
            if j > (i+2//N)%N:
                for l in range(j,N):
                    if l in idx_lst3:
                        idx_lst3.remove(l)
            else:
                for q in range(i, j):
                    if q in idx_lst3:
                        idx_lst3.remove(q)
            for k in idx_lst3:
                idx_lst4 = idx_lst3.copy()
                idx_lst4.remove(k)
                if k-1 in idx_lst4:
                    idx_lst4.remove(k-1)
                if k+1 in idx_lst4:
                    idx_lst4.remove(k+1)
                for p in idx_lst4:
                    abcd.append((i,j,k,p))
    print(abcd)
    for a,b,c,d in abcd:
        tmp = (arr[a]+arr[b])**2 + (arr[c]+arr[d])**2
        if max_v < tmp:
            max_v = tmp

    print(f'#{tc} {max_v}')
