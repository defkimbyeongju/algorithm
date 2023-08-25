T = int(input())
for tc in range(1,T+1):
    word_list = [list(input()) for _ in range(5)]
    word = ''
    max_len = 0
    for i in word_list:
        if max_len < len(i):
            max_len = len(i)

    for i in range(max_len):
        for j in range(5):
            try:
                word += word_list[j][i]
            except:
                continue

    print(f'#{tc} {word}')
