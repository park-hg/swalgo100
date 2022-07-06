import sys
sys.stdin = open('input.txt')
k = int(sys.stdin.readline())
ineqs = sys.stdin.readline().split()
visited = [False]*10
nums = []

def backtrack(d, num):
    if len(num) == k+1:
        nums.append(num)
        return

    for i in range(10):
        if not visited[i]:
            if eval(num[-1] + ineqs[d] + str(i)):
                visited[i] = True
                backtrack(d+1, num+str(i))
                visited[i] = False

for i in range(10):
    visited[i] = True
    backtrack(0, str(i))
    visited[i] = False

print(nums[-1])
print(nums[0])