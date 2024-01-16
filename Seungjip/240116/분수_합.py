a, b = map(int, input().split())
c, d = map(int, input().split())

ans1, ans2 = b*c+a*d, b*d

n1 = ans1
n2 = ans2
while n2 != 0:
    temp = n1
    n1 = n2
    n2 = temp%n2

print(ans1//n1, ans2//n1)