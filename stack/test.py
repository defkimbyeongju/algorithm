# def recursion(s, l, r):
#     global total
#     total += 1
#     if l >= r:
#         return 1
#     elif s[l] != s[r]:
#         return 0
#     else:
#         return recursion(s, l+1, r-1)
#
# def isPalindrome(s):
#     return recursion(s, 0, len(s)-1)
#
# T = int(input())
# for _ in range(T):
#     total = 0
#     text = input()
#     print(isPalindrome(text), total)

text = [list(input()) for _ in range(5)]
ans = ''
max_v = 0
for i in text:
    if max_v < len(i):
        max_v = len(i)
for i in range(max_v):
    for j in range(5):
        if len(text[j]) > i:
            ans += text[j][i]
        else:
            continue
print(ans)
