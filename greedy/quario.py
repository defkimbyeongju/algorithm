N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
tape = 0
for i in range(N):
    if arr[i] in range(tape):
        continue
    else:
        cnt+= 1
        tape = arr[i]+L
print(cnt)