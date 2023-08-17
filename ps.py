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
'''
n,m= map(int,input().split())
arr= []
for i in range(n):
    arr.append([int(x) for x in input().split()])
'''
tetroArr = [
    [[1,1,1,1],[0,0,0,0]],
    [[1,0],[1,0],[1,0],[1,0]], ### BLUE DONE

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
for i in range(len(tetroArr)):
    print("[%d]*[%d]"%(len(tetroArr[i]),len(tetroArr[i][0])))