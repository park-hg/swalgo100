import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
K -= 5

total = set()
words = []
for _ in range(N):
    word = set(sys.stdin.readline().rstrip())
    for m in ['a', 'c', 'i', 'n', 't']:
        word.remove(m)
    words.append(word)
    for a in word:
        total.add(a)
total = list(total)
visited = [False]*len(total)

answer = 0
def backtrack(start, k, alphas):
    print(alphas, start)
    global answer

    if k == K:
        cnt = 0
        for word in words:
            if word.issubset(alphas):
                cnt += 1
        answer = max(answer, cnt)
        return

    for i in range(start, len(total)):
        if not visited[i]:
            visited[i] = True
            backtrack(i, k+1, alphas+[total[i]])
            visited[i] = False

if K < 0:
    print(0)
elif len(total) <= K:
    print(N)
else:
    backtrack(0, 0, [])
    print(answer)