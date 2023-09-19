numbers = [1,2,3]
cnt = 0
def backtracking(total):
    global cnt
    if total == n:
        cnt += 1
        return
    if total > n:
        return
    for i in numbers:
        total += i
        backtracking(total)
        total -= i
n = int(input())
backtracking(0)
print(cnt)
