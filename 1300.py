import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

def func(x):
    s = 0
    for i in range(1, N+1):
        s += min(x//i, N)
    return s

left, right = 1, N**2
while left < right:
    mid = (left+right) // 2
    if func(mid) < K:
        left = mid+1
    else:
        right = mid

print(left)