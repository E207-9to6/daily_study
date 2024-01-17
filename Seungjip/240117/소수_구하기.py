def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

M, N = map(int, input().split())
if N == 2:
    print(2)
else:
    for i in range(M, N+1):
        if i == 1:
            continue
        if check(i):
            print(i)