M = int(input())
N = int(input())

prime_sum = 0
minimum_prime = 0

for num in range(M, N+1):
    if num == 1:
        continue
    if num == 2:
        minimum_prime = 2
        prime_sum += 2
    else:
        is_prime_flag = True
        start = 2
        while start <= num*(1/2):
            if num%start == 0:
                is_prime_flag = False
                break
            start += 1
        if is_prime_flag == True:
            prime_sum += num
            if minimum_prime == 0:
                minimum_prime = num

if minimum_prime == 0 and prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(minimum_prime)