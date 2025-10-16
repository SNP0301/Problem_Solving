/*
    긍정, 책임
    추억의 BFS 렛츠고
*/
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAXNM = 50;
static int arr[MAXNM][MAXNM] = {{0}};
static bool v[MAXNM][MAXNM] = {{false}};
static int N,M,answer;
static int dx[4] = {0,-1,0,1};
static int dy[4] = {-1,0,1,0};


bool isOut(int x, int y){
    if(x<0 || x>=N || y<0 || y>=M) return true;
    return false;
}

void clean(){
    for(int cx=0; cx<MAXNM; ++cx){
        for(int cy=0; cy<MAXNM; ++cy){
            arr[cx][cy] = 0;
            v[cx][cy] = false;
        }
    }
}

void BFS(int ix, int iy){
    queue<pair<int,int>> q;

    q.push(pair(ix,iy));
    v[ix][iy] = true;
    
    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int x = cur.first;
        int y = cur.second;

        for(int f=0; f<4; ++f){
            int nx = x + dx[f];
            int ny = y + dy[f];
            if (!isOut(nx,ny) && arr[nx][ny]==1 && !v[nx][ny]){ // 범위 내, 유효한 1, 미방문이면
                q.push({nx,ny});
                v[nx][ny] = true;

            }
        }


    }

}

int main(){
    int T,K,ix,iy;
    cin >> T;

    for(int t=0; t<T; ++t){
        cin >> M >> N >> K;
        
        // 새로운 밭에다가 애벌레 심기
        clean();
        answer = 0;

        for(int k=0; k<K; ++k){
            cin >> iy >> ix;
            arr[ix][iy] = 1;
        }

        //BFS 통해서 애벌레 수 세기
        for(int x=0; x<N; ++x){
            for(int y=0; y<M; ++y){
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