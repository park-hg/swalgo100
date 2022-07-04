import sys
from collections import deque
sys.stdin = open('input.txt')

stack = list(sys.stdin.readline().rstrip())
dq = deque()
M = int(sys.stdin.readline())
for _ in range(M):
    q = sys.stdin.readline().rstrip().split()
    if q[0] == 'L':
        if stack:
            dq.appendleft(stack.pop())
    elif q[0] == 'D':
        if dq:
            stack.append(dq.popleft())
    elif q[0] == 'B':
        if stack:
            stack.pop()
    elif q[0] == 'P':
        stack.append(q[1])

print(''.join(stack) + ''.join(dq))
