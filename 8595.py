import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
answer = 0
tmp = ''
for c in sys.stdin.readline().rstrip() + 'a':
    if c.isdigit():
        tmp += c
    else:
        if len(tmp) > 0:
            answer += int(tmp)
            tmp = ''

print(answer)