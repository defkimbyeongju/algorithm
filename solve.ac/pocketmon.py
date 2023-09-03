N, M = map(int, input().split())
pocketmon = {}
for i in range(N):
    pocketmon[input()] = i+1
pocket = dict(map(reversed, pocketmon.items()))
question = [input() for _ in range(M)]
for i in question:
    if i.isdigit():
        print(pocket.get(int(i)))
    else:
        print(pocketmon.get(i))
