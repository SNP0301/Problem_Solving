### https://doorbw.tistory.com/235 공부하기
def push_front(deque:list , X:int):
    xList = list()
    xList.append(X)
    print(type(xList))
    print(type(deque))
    deque = xList + deque

    return deque

def push_back(deque:list , X:int):
    return deque.append(X)

def pop_front(deque:list):
    if(not deque): 
       print(-1)
    else:
        print(deque[0])
        return deque[1:]

def pop_back(deque:list):
    if(not deque):
        print(-1)
    else:
        print(deque[len(deque)-1])
        return deque[:-1]
    
def size(deque:list):
    return len(deque)

def empty(deque:list):
    if(not deque):
        print(1)
    else:
        print(0)

def front(deque:list):
    if(not deque):
        print(-1)
    else:
        print(deque[0])

def back(deque:list):
    if(not deque):
        print(-1)
    else:
        print(deque[len(deque)-1])
       

import sys
input = sys.stdin.readline


n = int(input())
deque = []

for _ in range(n):
    command = list(map(str,input().split()))
    
    if(len(command)==2):
        X = int(command[1])

    if(command[0] == "push_front"):
        deque = push_front(*deque,X)
    elif(command[0] == "push_back"):
        deque = push_back(*deque,X)
    elif(command[0] == "pop_front"):
        deque = pop_front(*deque)
    elif(command[0] == "pop_back"):
        deque = pop_back(*deque)
    elif(command[0] == "size"):
        size(*deque)
    elif(command[0] == "empty"):
        empty(*deque)
    elif(command[0] == "front"):
        front(*deque)
    elif(command[0] == "back"):
        back(*deque)





