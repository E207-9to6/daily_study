N = int(input())
sigma = [0]* 10000
sum = 0

for i in range(1, N+1):
    sigma[i] = sigma[i-1] + i
    if sigma[i] >= N:
        sum = i+1
        break

start = sigma[sum-2] + 1
# print(sum)
# print(start)
# print(sigma)

# 순방향(1/6 -> 2/5 ...)
if sum%2:
    a = 0
    b = sum - a
    while 1:
        a += 1
        if start == N:
            break
        b = sum - a
        start += 1
    print(f'{a}/{b-1}')


# 역방향(6/1 -> 5/2 ...)
else:
    b = 0
    a = sum - b
    while 1:
        b += 1
        if start == N:
            break
        a = sum - b
        start += 1
    print(f'{a-1}/{b}')