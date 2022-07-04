import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = arr[0]
dp[1][0] = -1000
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1]+arr[i], arr[i])
for i in range(1, n):
    dp[1][i] = max(dp[1][i-1]+arr[i], dp[0][i-1])

print(max(max(dp[0]), max(dp[1])))
print(dp)