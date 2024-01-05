# 소인수 분해할 수 입력받기
N = int(input())
if N == 1:
    quit(0)

# 소인수를 찾으면 N을 변경하자.
start = 2
while start <= N*(1/2):
    if N%start == 0:
        N//=start
        print(start)
        start = 2
        continue
    start += 1
if start != 1:
    print(N)