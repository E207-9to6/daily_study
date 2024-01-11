# 시루는 가을에 입을 바지를 미리 사기 위해 백화점에 왔다. 
# 다리가 길고 저체중인 시루는 길이가 맞는 바지를 사면 허리가 너무 크고, 
# 허리가 맞는 바지를 사면 길이가 짧아서 잘 맞는 바지를 찾지 못하고 있다.

# 길이가 맞는 바지를 산 다음 허리둘레를 수선을 하거나 허리띠를 하면 되지만, 
# 수선하는 것은 귀찮고 허리띠를 불편해하는 시루는 멋진 아이디어를 생각해냈다. 
# 허리가 조금 크고 길이가 조금 짧은 바지를 산 다음, 
# 허리가 아닌 엉덩이에 바지를 걸치는 방식으로 입는 것이다.

# 지면에서 
# x 만큼 떨어진 시루의 하체 둘레는 
# f(x) = max(a(x-b)^2+c, d)로 계산할 수 있다. 예를 들어 
# f(x) = max(-0.1(x-50)^2+10, 6)이라고 하면, 시루가 엎드려 있을 때 하체는 다음과 같은 형태이다.

# 바지가 땅에 끌리지 않고, 바지의 끝부분의 높이가 지면과 일치하는 바지의 개수
import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())



N = int(input())
count = 0

for _ in range(N):
    u, v = map(int, input().split())
    
    circumference = max(a*(v-b)**2+c, d)
    if u == circumference:
        count += 1

print(count)