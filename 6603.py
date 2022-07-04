import sys
from itertools import combinations
sys.stdin = open('input.txt')

while True:
    line = list(map(int, sys.stdin.readline().split()))
    if line[0] == 0:
        break

    for comb in combinations(line[1:], 6):
        print(*comb)
    print()