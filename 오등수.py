#19722 오등수

N = int(input())
seq = list(map(int, input().split()))

O_num = [-1] * N
F = [0] * N

stack = []

for i in seq:
    F[i] += 1


for i in range(N):
    #오큰수가 존재할경우 
    while len(stack) and F[seq[i]] > F[seq[stack[-1]]]:
        
        O_num[stack.pop()] = seq[i]

    #오큰수 없을경우 
    stack.append(i)

for i in O_num:
    print(i, end=' ')