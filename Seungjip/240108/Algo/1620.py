N, M = map(int, input().split())
poketmons = []
for _ in range(N):
    name = input()
    poketmons.append(name)
answer = []
for _ in range(M):
    ans = input()
    answer.append(ans)
    try :
        ans = int(ans)
        print(poketmons[ans-1])
    
    except:
        fin = poketmons.index(ans)
        print(fin+1)