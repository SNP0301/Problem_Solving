import sys
input = sys.stdin.readline

n = int(input())
arr = list() ## works as a map
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    global cnt
    queue = [(x,y)]
    arr[x][y] = 0

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
        
            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= n:
                continue
            
            if arr[nextX][nextY] == 1:
                queue.append((nextX, nextY))
                arr[nextX][nextY] = 0
                cnt += 1

dong = list() ## works as a cnt

for _ in range(n):
    line = input().rstrip()
    ##print(line)
    arr.append([int(x) for x in line])

for l in range(n):
    for m in range(n):
        if arr[l][m] == 1:
            BFS(l,m)
            ##print("from (%d,%d), %d was appended"%(l,m,cnt+1))
            dong.append(cnt+1)
            cnt = 0
            


dong.sort()
dongNum = len(dong)

print(dongNum)

for i in range(dongNum):
    print(dong[i])


