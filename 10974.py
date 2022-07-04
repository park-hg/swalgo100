import sys
from itertools import permutations
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
for perm in permutations(range(1, N+1), N):
    print(*perm)