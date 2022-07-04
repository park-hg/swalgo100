import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))


def func(x):
    cnt = 1
    tmp = 0
    for i in range(len(t)):
        tmp += t[i]
        if tmp > x:
            cnt += 1
            tmp = t[i]

    return cnt


left, right = max(t), sum(t)

while left < right:
    mid = (left+right) // 2
    if func(mid) > M:
        left = mid+1
    else:
        right = mid

print(left)
