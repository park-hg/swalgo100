import sys
sys.stdin = open('input.txt')
k = int(sys.stdin.readline())
ineqs = sys.stdin.readline().split()
visited = [False]*10
nums = []
def backtrack(d, num):
    print(num)
    if len(num) == k+1:
        nums.append(num)
        return

    for i in range(10):
        if not visited[i]:
            if not num or eval(num[-1] + ineqs[d] + str(i)):
                visited[i] = True
                backtrack(d+1, num+str(i))
                visited[i] = False


backtrack(0, "")
print(nums)