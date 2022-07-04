from re import L
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, N):
    for j in range(1, K+1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % (10**9+3)

dp[N][K] = (dp[N-1][K] + dp[N-3][K-1]) % (10**9+3)
print(dp[N][K])