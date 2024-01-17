def check(p):
    for i in range(2, int(p**(1/2))+1):
        if p%i == 0:
            return False
    return True

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for j in range(N+1, 2*N+1):
        if check(j):
            cnt += 1
    print(cnt)