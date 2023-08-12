def ispalindrome(txt):
    if txt == txt[::-1]:
        return 0
    else:
        k = len(txt)
        for i in range(k//2):
            if not txt[i] == txt[k-i-1]:
                if txt[i] == txt[k-i-2]:
                    del txt[k-i-1]
                    if txt == txt[::-1]:
                        return 1
                    else:
                        return 2
                elif txt[i-1] == txt[k-i-1]:
                    del txt[i]
                    if txt == txt[::-1]:
                        return 1
                    else:
                        return 2
                else:
                    return 2
        return 2

n = int(input())
for _ in range(n):
    txt = list(input())
    print(ispalindrome(txt))
