N = int(input())
numbers = list(map(int, input().split()))

# print(numbers)
cnt = 0

for num in numbers:
    is_prime_flag = True
    if num == 1:
        continue
    start = 2
    while start <= (num)*(1/2):
        if num%start == 0:
            is_prime_flag = False
            break
        start += 1
    if is_prime_flag == True:
        cnt += 1

print(cnt)