import sys
sys.stdin = open('input.txt')

K, N = map(int, sys.stdin.readline().split())

l = [int(sys.stdin.readline()) for _ in range(K)]

def func(x):
    return sum([i//x for i in l])

left, right = 0, 2**31
while left < right:
    mid = (left+right) // 2
    if func(mid) >= N:
        left = mid+1
    else:
        right = mid

print(left-1)