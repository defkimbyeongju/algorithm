def ispalindrome(t):
    if t == t[::-1]:
        return 0
    else:
        for i in range(len(t)):
            if t[i] != t[len(t)-1-i]:
                if t.replace(t[i], '') == t.replace(t[i], '')[::-1]:
                    return 1
                elif t.replace(t[len(t)-1-i], '') == t.replace(t[len(t)-1-i], '')[::-1]:
                    return 1
        return 2

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    data = input().rstrip()
    print(ispalindrome(data))
