import sys
from collections import deque
sys.stdin = open('input.txt')
S = int(sys.stdin.readline())

visited = [[False]*(S+1) for _ in range(S+1)]
visited[1][0] = True
que = deque([(1, 0, 0)])
while que:
    num, copied, cnt = que.popleft()
    if num == S:
        print(cnt)
        break

    if 1 <= num-1 <= S:
        if not visited[num-1][copied]:
            que.append((num-1, copied, cnt+1))
            visited[num-1][copied] = True

    if 1 <= num <= S:
        if num != copied:
            if not visited[num][num]:
                que.append((num, num, cnt+1))
                visited[num][num] = True
    
    if copied > 0:
        if 0 <= num+copied <= S:
            if not visited[num+copied][copied]:
                que.append((num+copied, copied, cnt+1))
                visited[num+copied][copied] = True

