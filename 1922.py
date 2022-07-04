import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key=lambda x:x[-1])

par = list(range(N+1))
rank = [0]*(N+1)

def find(x):
    if par[x] == x:
        return x
    return find(par[x])

def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    
    if rank[x] < rank[y]:
        par[x] = y
    else:
        if rank[x] == rank[y]:
            rank[x] += 1
        par[y] = x

def same(x, y):
    return find(x) == find(y)

ans = 0
for a, b, c in edges:
    if not same(a, b):
        unite(a, b)
        ans += c

print(ans)