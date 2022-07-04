import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
is_prime = [True]*10000
is_prime[0] = False
is_prime[1] = False

for i in range(10000):
    if is_prime[i]:
        for j in range(2*i, 10000, i):
            is_prime[j] = False


for _ in range(T):
    visited = [False]*10000
    A, B = map(int, sys.stdin.readline().split())
    que = deque([(A, 0)])
    ans = -1
    while que:
        num, cnt = que.popleft()
        if num == B:
            ans = cnt
            break
        for i in range(1, 10):
            new_num = int(str(i)+str(num)[1:])
            if new_num != num and not visited[new_num] and is_prime[new_num]:
                que.append((new_num, cnt+1))
                visited[new_num] = True
        
        for j in range(1, 4):
            for i in range(10):
                new_num = int(str(num)[:j] + str(i) + str(num)[j+1:])
                if new_num != num and not visited[new_num] and is_prime[new_num]:
                    que.append((new_num, cnt+1))
                    visited[new_num] = True

    if ans == -1:
        print('Impossible')
    else:
        print(ans)