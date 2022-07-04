import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

R, C = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]

def dfs(x, y):
    if y == C-1:
        return True

    visited[x][y] = True

    for dx in [-1, 0, 1]:
        nx, ny = x+dx, y+1
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
            if grid[nx][ny] == ".":
                if dfs(nx, ny):
                    return True

    return False

ans = 0
for i in range(R):
    if not visited[i][0]:
        if dfs(i, 0):
            ans += 1

print(ans)