import sys
from collections import defaultdict, deque
from heapq import *
sys.stdin = open('input.txt')
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    S, D = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(M):
        U, V, P = map(int, sys.stdin.readline().split())
        graph[U].append((V, P))

    prev = [0]*N
    d = [10**9]*N
    heap = [(0, S)]
    d[S] = 0
    answer = []
    while heap:
        cost, v = heappop(heap)
        if d[v] < cost:
            continue
        for w, c in graph[v]:
            if d[w] < d[v] + c:
                continue
            d[w] = d[v] + c
            heappush(heap, (d[w], w))

    