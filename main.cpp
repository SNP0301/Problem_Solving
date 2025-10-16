/*
    긍정, 책임
    8방인접 bfs

    -1-1  -10  -11
     0-1   00  >01<
     1-1   10   11
*/
#include <iostream>
#include <queue>
using namespace std;

const int ex[8] = {0,1,1,1,0,-1,-1,-1};
const int ey[8] = {1,1,0,-1,-1,-1,0,1};
const int MAXSIZE = 50+1;
static int w,h;
static int arr[MAXSIZE][MAXSIZE] = {{0}};
static bool v[MAXSIZE][MAXSIZE] = {{false}};

void clean(){
    for(int x=0; x<MAXSIZE; ++x){
        for(int y=0; y<MAXSIZE; ++y){
            arr[x][y] = 0;
            v[x][y] = false;
        }
    }
}

bool outofBound(int x, int y){
    return (x<0 || x >= h || y<0 || y >= w);
}

void BFS(int x, int y){
    queue<pair<int,int>> q;
    q.push({x,y});
    v[x][y] = true;

    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int ix = cur.first;
        int iy = cur.second;
        for(int e=0; e<8; ++e){ // e for eight
            int nx = ix + ex[e];
            int ny = iy + ey[e];
            if(!outofBound(nx,ny) && !v[nx][ny] && arr[nx][ny]==1){ // 범위 내, 미방문, 조건 만족하면
                q.push({nx,ny});
                v[nx][ny] = true;
            }
        }

    }

}

int main(){
    int num;
    while (true){
        clean();
        cin >> w >> h;
        if(w==0 && h==0) break; // 입력의 마지막에는 0이 2개 주어진다

        // 정답, 지도, 방문 배열 초기화
        int answer = 0;


        for(int x=0; x<h; ++x){
            for(int y=0; y<w; ++y){
                cin >> num;
                arr[x][y] = num;
            }
        }

        for(int x=0; x<h; ++x){
            for(int y=0; y<w; ++y){
                if(arr[x][y]==1 && !v[x][y]){
                    BFS(x,y);
                    answer += 1;
                }
            }
        }

        cout << answer << "\n";




    }

    return 0;
}