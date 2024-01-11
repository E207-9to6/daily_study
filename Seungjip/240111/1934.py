N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    n1 = a
    n2 = b
    while n2 != 0:
        temp = n1
        n1 = n2
        n2 = temp % n2

    print(a * b // n1)