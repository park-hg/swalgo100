import sys
sys.stdin = open('input.txt')

s = list(sys.stdin.readline().rstrip())
p = list(sys.stdin.readline().rstrip())

stack = []
for c in s:
    stack.append(c)
    while len(stack) >= len(p) and stack[-len(p):] == p:
        for _ in range(len(p)):
            stack.pop()
    
print('FRULA' if len(stack) == 0 else ''.join(stack))