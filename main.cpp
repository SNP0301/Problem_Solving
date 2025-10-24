/*
    긍정, 책임

    추억이 새록새록
    8*8*8경우의 수에 대해 8*8 완전탐색
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int arr[8][8];
int fx[4] = {0,0,-1,1};
int fy[4] = {-1,1,0,0};
int N,M;
vector<pair<int,int>> virusVc;

bool outofBound(int x, int y){return(x<0 || x>=N || y<0 || y>=M);}

int BFS(){
    int ret = 0;

    // 0. 바이러스 다 넣고 BFS 돌리기
    bool v[N][M];
    int bfsArr[N][M];
    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            bfsArr[x][y] = arr[x][y];
            v[x][y] = false;
        }
    }

    queue<pair<int,int>> q;
    for(auto virus: virusVc){
        int vx = virus.first;
        int vy = virus.second;
        q.push({vx,vy});
        v[vx][vy] = true;
    }

    while(!q.empty()){
        auto [x,y] = q.front(); q.pop();
        for(int f=0; f<4; ++f){
            int nx = x + fx[f];
            int ny = y + fy[f];

            if(!outofBound(nx,ny) && !v[nx][ny] && bfsArr[nx][ny]==0){
                q.push({nx,ny});
                v[nx][ny] = true;
                bfsArr[nx][ny] = 2;
            }
        }
    }

    // 1. BFS 결과에 대해 0 세기
    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            if (bfsArr[x][y] == 0) ++ret;
        }
    }

    return ret;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int state;
    int answer = 0;
    int cur_ans = 0;
    cin >> N >> M;

    for(int x=0; x<N; ++x){
        for(int y=0; y<M; ++y){
            cin >> state;
            arr[x][y] = state;
            if (arr[x][y]==2){
                virusVc.push_back({x,y});
            }
        }
    }

    for(int first=0; first<N*M-2; ++first){
        if(arr[first/M][first%M]!=0) continue;
        for(int second=first+1; second<N*M-1; ++second){
            if(arr[second/M][second%M]!=0) continue;
            for(int third=second+1; third<N*M; ++third){
                if(arr[third/M][third%M]!=0) continue;
                int cand[3] = {first,second,third};

                for(auto num: cand){
                    arr[num/M][num%M] = 1;
                }
                cur_ans = BFS();

                for(auto num: cand){
                    arr[num/M][num%M] = 0;
                }
                answer = max(answer,cur_ans);
            }
        }
    }

    cout << answer;

    return 0;
}