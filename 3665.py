import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    t = list(map(int, sys.stdin.readline().split()))
    graph = defaultdict(list)
    indegree = [0]*(n+1)
    for i in range(n-1):
        for j in range(i+1, n):
            graph[t[i]].append(t[j])
            indegree[t[j]] += 1
    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        else:
            graph[a].remove(b)
            indegree[a] += 1
            graph[b].append(a)
            indegree[b] -= 1
    
    que = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
    
    if len(que) > 1:
        print("?")
        continue
    
    discovered = []
    while que:
        v = que.popleft()
        discovered.append(v)
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                que.append(w)

    if len(discovered) == n:
        print(*discovered)
    else:
        print("IMPOSSIBLE")
    
