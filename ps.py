import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = list()
areaArr = list()
visitedDfs = [[False]*n for _ in range(n)]
accum = 1
cnt = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(input().split())

def dfs(x,y):
    visitedDfs[x][y] = True

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0:
            continue
        if visitedDfs[nextX][nextY] == False and newGraph[x][y] == 1:
            dfs(nextX, nextY)
    
while True:
    searched = False

    area = 0
    visitedDfs = [[False]*n for _ in range(n)]
    line = list()
    newGraph = list()

    ##print(accum)
    ### Create a new graph with the current graph
    for a in range(n):
        for b in range(n):
            if int(graph[a][b]) > accum:
                line.append(1)
            else:
                line.append(0)
        newGraph.append(line)
        line = list()

    ##print(newGraph)

    ### DFS
    a = 0
    b = 0
    for a in range(n):
        for b in range(n):
            if not visitedDfs[a][b] and newGraph[a][b] == 1:
                dfs(a,b)
                area += 1
                searched = True

    if searched:
        areaArr.append(area)
        accum += 1
        cnt += 1

    else:
        print(max(areaArr))
        break