"""
arr 안 쓰는게 더 시간/공간 측면에서 좋을 것.


[개인]
    - 급하면 arr부터 세우고 보는 습관 버리기..
        - FTR) Z
    - x,y축 지금이라도 바꿔야하나?
"""

start = list(input().split())

## ord("A") = 65
## ord("H") = 72

kx,ky = 8-int(start[0][1]), ord(start[0][0])-65## king 시작점 
sx,sy = 8-int(start[1][1]), ord(start[1][0])-65## stone 시작점


def my_print(a):
    for x in a:
        print(x)
    print()
arr = [[0 for _ in range(8)] for _ in range(8)]
arr[kx][ky] = "K"
arr[sx][sy] = "S"
#print(kx,ky)
#print(sx,sy)
#my_print(arr)

for _ in range(int(start[2])):
    cmd = input()
    #print(cmd)
    if cmd == "B":
        if 0<=kx+1<8 and 0<=ky<8:
            if arr[kx+1][ky] == "S":
                if 0<=sx+1<8:
                    arr[sx][sy] = 0
                    sx = sx+1
                    arr[kx][ky] = 0
                    kx = kx+1

            elif arr[kx+1][ky] != "S":
                arr[kx][ky] = 0
                kx = kx+1

    elif cmd == "L":
        if 0<=kx<8 and 0<=ky-1<8:
            if arr[kx][ky-1] == "S":
                if 0<=sy-1<8:
                    arr[sx][sy] = 0
                    sy = sy-1
                    arr[kx][ky] = 0
                    ky = ky-1
            else:
                arr[kx][ky] = 0
                ky = ky-1
    elif cmd == "R":
        if 0<=kx<8 and 0<=ky+1<8:
            if arr[kx][ky+1] == "S":
                if 0<=sy+1<8:
                    arr[sx][sy] = 0
                    sy = sy+1
                    arr[kx][ky] = 0
                    ky = ky+1
            else:
                arr[kx][ky] = 0
                ky = ky+1
    elif cmd == "T":
        if 0<=kx-1<8 and 0<=ky<8:
            if arr[kx-1][ky] == "S":
                if 0<=sx-1<8:
                    arr[sx][sy] = 0
                    sx -= 1
                    arr[kx][ky] = 0
                    kx -= 1
            else:
                arr[kx][ky] = 0
                kx -= 1
    elif cmd == "RT":
        if 0<=kx-1<8 and 0<=ky+1<8:
            if arr[kx-1][ky+1] == "S":
                if 0<=sx-1<8 and 0<=sy+1<8:
                    arr[sx][sy] = 0
                    sx -= 1
                    sy += 1
                    arr[kx][ky] = 0
                    kx -= 1
                    ky += 1
            else:
                arr[kx][ky] = 0
                kx -= 1
                ky += 1
    elif cmd == "LT":
        if 0<=kx-1<8 and 0<=ky-1<8:
            if arr[kx-1][ky-1] == "S":
                if 0<=sx-1<8 and 0<=sy-1<8:
                    arr[sx][sy] = 0
                    sx -= 1
                    sy -= 1
                    arr[kx][ky] = 0
                    kx -= 1
                    ky -= 1
            else:
                arr[kx][ky] = 0
                kx -= 1
                ky -= 1
    elif cmd == "RB":
        if 0<=kx+1<8 and 0<=ky+1<8:
            if arr[kx+1][ky+1] == "S":
                if 0<=sx+1<8 and 0<=sy+1<8:
                    arr[sx][sy] = 0
                    sx += 1
                    sy += 1
                    arr[kx][ky] = 0
                    kx += 1
                    ky += 1
            else:
                arr[kx][ky] = 0
                kx += 1
                ky += 1
    elif cmd == "LB":
        if 0<=kx+1<8 and 0<=ky-1<8:
            if arr[kx+1][ky-1] == "S":
                if 0<=sx+1<8 and 0<=sy-1<8:
                    arr[sx][sy] = 0
                    sx += 1
                    sy -= 1
                    arr[kx][ky] = 0
                    kx += 1
                    ky -= 1
            else:
                arr[kx][ky] = 0
                kx += 1
                ky -= 1

    arr[kx][ky] = "K"
    arr[sx][sy] = "S"
  
    #my_print(arr)
y_arr = ["","A","B","C","D","E","F","G","H",""]
print(y_arr[ky+1],end="")
print(8-kx)
print(y_arr[sy+1],end="")
print(8-sx)