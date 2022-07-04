import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

crossed = 0

def merge(A, B):
    global crossed
    merged = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            crossed += (len(A)-i)
            j += 1
    
    if i < len(A):
        merged += A[i:]
    elif j < len(B):
        merged += B[j:]

    return merged

def merge_sort(L):
    if len(L) <= 1:
        return L

    mid = len(L)//2
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

merge_sort(A)
print(crossed)