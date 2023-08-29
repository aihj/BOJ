import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque([])

for i in range(N):
    command = input().split()
    
    if command[0] == "push_front": 
        queue.appendleft(int(command[1])) ## 앞에 넣기
    
    elif command[0] == "push_back":
        queue.append(int(command[1])) ## 뒤에 넣기
     
    elif command[0] == "pop_front":
        if queue:
            print (queue.popleft()) ## 앞에서 뺴기
        else:
            print (-1)

    elif command[0] == "pop_back":
        if queue:
            print (queue.pop()) ## 뒤에서 뺴기 
        else:
            print (-1)
    
    elif command[0] == "size":
        print (len(queue))
    
    elif command[0] == "empty": ## 비어있으면 1, 아니면 0
        if queue:
            print (0)
        else:
            print (1)

    elif command[0] == "front": 
        if queue:
            print (queue[0])
        else:
            print (-1)
        
    elif command[0] == "back":
        if queue:
            print (queue[-1])
        else:
            print (-1)