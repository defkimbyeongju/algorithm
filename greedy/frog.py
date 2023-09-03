
N, Q = map(int, input().split())
tree = []
for i in range(N):
    x1, x2, y = map(int, input().split())
    tree.append([x1,x2,y,i])

tree.sort(key=lambda x:x[0])
for _ in range(Q):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    cnt = 1

    while start < end:
        if tree[start+cnt][0] <= tree[start][1] <= tree[start+cnt][1]:
            start = start+cnt
            cnt = 1
        else:
            cnt += 1