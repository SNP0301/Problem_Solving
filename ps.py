'''
[BOJ] 14500. 테트로미노

1. Blue: 2가지
2. Yellow: 1가지
3. Orange: 8가지
4. Green: 4가지
5. Pink: 4가지
'''

import sys
input = sys.stdin.readline

n,m= map(int,input().split())
arr= []
for i in range(n):
    arr.append([int(x) for x in input().split()])

tetroArr = [
    [[1,1,1,1]],
    [[1],[1],[1],[1]], ### BLUE DONE

    [[1,1],[1,1]], ### Yellow DONE

    [[1,0],[1,0],[1,1]],
    [[0,1],[0,1],[1,1]],
    [[1,1],[1,0],[1,0]],
    [[1,1],[0,1],[0,1]],

    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
    [[1,1,1],[1,0,0]],
    [[1,1,1],[0,0,1]], ### ORANGE DONE

    [[1,0],[1,1],[0,1]],
    [[0,1],[1,1],[1,0]],

    [[0,1,1],[1,1,0]],
    [[1,1,0],[0,1,1]], ### GREEN DONE

    [[1,1,1],[0,1,0]],
    [[0,1,0],[1,1,1]],
    
    [[1,0],[1,1],[1,0]],
    [[0,1],[1,1],[0,1]] ### PINK DONE


]

'''
for i in range(len(tetroArr)):
   print("CHECK BOUNDARY: DOWN[%d], and RIGHT[%d]"%(len(tetroArr[i])-1,len(tetroArr[i][0])-1))

down boundary = len(tetroArr[i])-1
right boundary = len(tetroArr[i][0])-1
'''

print("%dX%d"%(n,m))

iStart = 0
jStart = 0
tetroType = 0
max = -1
ti = 0
tj = 0

while(iStart<=n-1 and jStart<=m-1):
    print("Starts from [%d,%d]"%(iStart,jStart))
    for t in range(len(tetroArr)-17):
        if(len(tetroArr[t])-1<=n and len(tetroArr[t][0])-1<=m):
            print("End at [%d,%d]"%(len(tetroArr[t])-1,len(tetroArr[t][0])-1))
                

    if(jStart==m-1):
        iStart += 1
        jStart = 0
    else:
        jStart += 1

