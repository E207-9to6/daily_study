N, M = map(int, input().split())

idx = 0
factor = 1

while factor <= N:
    if N % factor == 0:
        idx += 1
    if idx == M:
        print(factor)
        break
    factor += 1

if idx < M:
    print(0)