import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

t = [0]*(N+1)
graph = defaultdict(list)
indegree = [0]*(N+1)
for v in range(1, N+1):
    line = list(map(int, sys.stdin.readline().split()))
    t[v] = line[0]
    for w in line[1:-1]:
        graph[w].append(v)
    indegree[v] += len(line[1:-1])

dp = [0]*(N+1)
que = deque()
for v in range(1, N+1):
    if indegree[v] == 0:
        que.append(v)
        dp[v] = t[v]

while que:
    v = que.popleft()
    for w in graph[v]:
        indegree[w] -= 1
        dp[w] = max(dp[w], dp[v]+t[w])
        if indegree[w] == 0:
            que.append(w)

for d in dp[1:]:
    print(d)