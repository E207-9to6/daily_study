N, Q = map(int, input().split())

stick_info = []

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    stick_info.append((a, b, i))

stick_info.sort(key=lambda x: (x[0], -x[1]))
# print(stick_info)

# 인접행렬 생성
adj = [[] for _ in range(N+1)]
idx = 0

# 만약 출발이 같다면 합치자
start = stick_info[0][0]
end = stick_info[0][1]
for tuple in stick_info:
    # 만약 출발점이 같다면 연결
    if tuple[0] == start:
        adj[idx].append(tuple[2])
        continue
    # 출발점이 다른데 이전의 end보다 작거나 같다면 연결
    if tuple[0] <= end:
        adj[idx].append(tuple[2])
        start = tuple[0]
        end = max(end, tuple[1])
        continue
    # 출발 점이 다르고 새로운 발판인 경우
    else:
        idx += 1
        adj[idx].append(tuple[2])
        start = tuple[0]
        end = tuple[1]

# print(adj)

for _ in range(Q):
    send, sent = map(int, input().split())
    is_connected_flag = False
    include_arr = []
    for arr in adj:
        if send in arr:
            include_arr = arr
            break
    if sent in arr:
        print(1)
    else:
        print(0)