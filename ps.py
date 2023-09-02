import sys
input = sys.stdin.readline

n,k = map(int,input().split())
queue = list()
popQueue = list()

for i in range(1,n+1):
    queue.append(i)

##print(queue)

while queue:
    queueLen = len(queue)
    if(queueLen == 1):
        popQueue.append(queue.pop(0))
    elif(queueLen >= k):
        popQueue.append(queue.pop(k-1))
        for j in range(k-1):
            queue.append(queue.pop(0))
    else:
        popQueue.append(queue.pop(k-1-(queueLen%k)))

print("<",end="")
for i in range(n-1):
    print(popQueue[i], end=", ")
print(popQueue[-1],end="")
print(">")