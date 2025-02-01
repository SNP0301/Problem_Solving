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

my_print(arr)

while True: #한번 돌 때 마다 128 -> 64 -> ... 으로 사이즈 줄여가며 탐색
    sz = sz//2
    print(sz)

    for start_x in range(N//sz):
        for start_y in range(N//sz):
            #print(start_x*sz,start_y*sz)
            for x in range(start_x,start_x+sz):
                for y in range(start_y,start_y+sz):
                    print(x,y)
            print("####")

    print()

    if sz == 1:
        break