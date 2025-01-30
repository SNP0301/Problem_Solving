"""

"""

def my_print(a):
    for x in a:
        print(x)
    print()


N = int(input())
target = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
c_cnt = 0
for i in range(N,0,-2):
    #print("doing %d"%i)
    cur = i**2
    cnt = 0
    x = (N-i)//2
    y = (N-i)//2
    arr[x][y] = cur
    if cur == target:
        x_answer = (N-i)//2+1
        y_answer = (N-i)//2+1
    if i == 1:
        break


    for f in range(4):
        for e in range(1,i):
            nx = x + dx[f]*e
            ny = y + dy[f]*e
            if 0<=nx<N and 0<=ny<N:

                if nx == (N-i)//2 and ny == (N-i)//2:
                    break
                else:
                    cur -= 1
                    arr[nx][ny] = cur
                    if cur == target:
                        x_answer = nx+1
                        y_answer = ny+1
                #my_print(arr)

        x = nx
        y = ny






for i in arr:
    for x in i:
        print(x,end=" ")
    print()
print(x_answer,y_answer)
