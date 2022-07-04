import sys
sys.stdin = open('input.txt')
N, L = map(int, sys.stdin.readline().split())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
info.sort()

ans = 0
s = info[0][0]
for a, b in info:
    start = max(a, s)
    if (b-start)%L == 0:
        c = (b-start)//L
    else:
        c = (b-start)//L + 1

    ans += c
    s = start + c*L

print(ans)
