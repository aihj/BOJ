#17298 오큰수
#스택 이용 LIFO

n = int(input())

seq = list(map(int, input().split()))

o_num = [-1] * n
stack = []

for i in range(n):

    #오큰수일 경우는, stack의 idx에 해당하는 seq을 계속 seq으로 바꿔준다.
    while stack and (stack[-1][0] < seq[i]):
        _, idx = stack.pop() 
        o_num[idx] = seq[i]

    # stack[-1][0] >= seq[i]인 경우 즉 아래가 위보다 큰 경우 
    stack.append([seq[i],i])

    print(stack)

print(*o_num)
