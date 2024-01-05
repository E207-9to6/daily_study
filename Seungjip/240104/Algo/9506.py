while True:
    N = int(input())
    if N == -1:
        break
    factor = []
    start = 1
    while start <= N:
        if N % start == 0:
            factor.append(str(start))
        start += 1
    if sum(map(int, factor)) == 2 * N:
        factor.pop()
        string = ' + '.join(factor)
        print(N, "=", string)
    else:
        print(f'{N} is NOT perfect.')
