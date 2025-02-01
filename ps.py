"""
[복잡도] O(n^2)? O(nlgn)??
- K=7이어서 전체 종이 크기가 128*128인 경우
    - 128*128 사이즈 1번 탐색
    - 64*64 사이즈 4번 탐색
    - 32*32 사이즈 16번 탐색
    - ...
    - (2**14개에 7번 접근) * 2 (0,1을 각각 탐색)
"""
def my_print(a):
    for x in a:
        print(x)
    print()

N = int(input())
sz = N*2
arr = [list(map(int,input().split())) for _ in range(N)]

blue = 0
white = 0
while True: #한번 돌 때 마다 128 -> 64 -> ... 으로 사이즈 줄여가며 탐색
    sz = sz//2

    for start_x in range(0,N,sz):
        for start_y in range(0,N,sz):
            #print("FROM: [%d,%d]"%(start_x,start_y))
            valid = True
            for x in range(start_x,start_x+sz):
                for y in range(start_y,start_y+sz):
                    if arr[x][y] != 1:
                        valid = False
            #print("END: [%d,%d]"%(start_x,start_y))
            if valid:
                for x in range(start_x,start_x+sz):
                    for y in range(start_y,start_y+sz):
                        arr[x][y] = -1
                blue += 1

    for start_x in range(0,N,sz):
        for start_y in range(0,N,sz):
            #print("FROM: [%d,%d]"%(start_x,start_y))
            valid = True
            for x in range(start_x,start_x+sz):
                for y in range(start_y,start_y+sz):
                    if arr[x][y] != 0:
                        valid = False
            #print("END: [%d,%d]"%(start_x,start_y))
            if valid:
                for x in range(start_x,start_x+sz):
                    for y in range(start_y,start_y+sz):
                        arr[x][y] = -1
                white += 1
    if sz == 1:
        break

print(white)
print(blue)