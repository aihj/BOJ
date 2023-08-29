import sys

N = int(sys.stdin.readline())

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.insert(0, cmd[1])
        ##print(queue)

    elif cmd[0] == "pop": ## 들어있는 정수 없으면 -1 출력
        if len(queue) != 0: print(queue.pop())
        else: print(-1) 

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty": ## 비어있으면 1, 아니면 0
        if len(queue) == 0: print(1)
        else : print(0) 

    elif cmd[0] == "front": ## 가장 앞의 정수 출력, 없으면 -1
        if len(queue) == 0: print(-1)
        else: print(queue[len(queue) -1])

    elif cmd[0] == "back": ## 가장 뒤의 정수 출력, 없으면 -1
        if len(queue) == 0: print(-1)
        else: print(queue[0])