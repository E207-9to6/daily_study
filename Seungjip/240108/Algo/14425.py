N, M = map(int, input().split())
standard = []
for _ in range(N):
    word = input()
    standard.append(word)

cnt = 0
for _ in range(M):
    check = input()
    if check in standard:
        cnt += 1
print(cnt)