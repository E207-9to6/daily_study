def findprime(num):
    standard = 2
    is_prime = True
    while standard <= num*(1/2):
        if num%standard == 0:
            is_prime = False
            break
        standard += 1
    return is_prime

N = int(input())
for _ in range(N):
    num = int(input())
    # num 보다 크거나 같은 수 중 가장 작은 소수 찾기
    while True:
        if num%2 == 0:
            continue
        if num%3 == 0:
            continue
        if findprime(num) == True:
            print(num)
            break
        num += 1